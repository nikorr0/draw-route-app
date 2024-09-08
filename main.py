from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QDialog, QLabel,
                               QPushButton, QGraphicsScene, 
                               QWidget, QMainWindow, QColorDialog,
                               QTableWidgetItem)

import sys
import ast
import os.path
import json

from ui_mainwindow import Ui_DrawRouteApp
from ui_resultwindow import Ui_Result
from ui_errorwindow import Ui_Error
from ui_customizationwindow import Ui_Customization
from ui_tooltipwindow import Ui_Tooltip

from packages.get_route_map_precise import draw_area_map_route_precise
from packages.get_route_map_multiple import draw_area_map_route_multiple
from packages.classify_points import classify_points
from packages.get_predicted_traveled_time import predict_traveled_time


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_DrawRouteApp()
        self.ui.setupUi(self)

        self.result_windows_list = list()
        
        self.ui.dateTimeEdit.hide()
        self.mode = "one_route"
        self.ui.coordinates_text.setText("[(), ()]")
        
        self.ui.submit_button.clicked.connect(self.submit)
        self.ui.customize_button.clicked.connect(self.customize)

        self.ui.one_route_radio.clicked.connect(self.show_additional_one) 
        self.ui.multiple_routes_radio.clicked.connect(self.hide_additional_multiple)
        self.ui.travel_time_checkbox.clicked.connect(self.hide_show_datetime)
        self.ui.tooltip_button.clicked.connect(self.show_tooltip)

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()
            
    @Slot()
    def hide_show_datetime(self):
        if self.ui.travel_time_checkbox.isChecked():
            self.ui.dateTimeEdit.show()
        else: 
            self.ui.dateTimeEdit.hide()
    
    @Slot()
    def hide_additional_multiple(self):
        coordinates = self.ui.coordinates_text.text()
        self.mode = "multiple_routes"
        if coordinates.strip() == "[(), ()]"\
            or (coordinates.strip() == ""):
            self.ui.coordinates_text.setText("[[(), ()], [(), ()]]")
        self.ui.one_route_widget.hide()
    
    @Slot()
    def show_additional_one(self):
        coordinates = self.ui.coordinates_text.text()
        self.mode = "one_route"
        if (coordinates.strip() == "[[(), ()], [(), ()]]")\
            or (coordinates.strip() == ""):
            self.ui.coordinates_text.setText("[(), ()]")
        self.ui.one_route_widget.show()

    @Slot()
    def show_tooltip(self):
        self.ui.tooltip_button.setEnabled(False)
        self.tooltip_window = TooltipWindow(self.ui.tooltip_button)
        self.tooltip_window.show()
        
    @Slot()
    def customize(self):
        self.ui.customize_button.setEnabled(False)
        
        coordinates = self.ui.coordinates_text.text()
        coordinates = self.convert_string_array(coordinates.strip(), self.mode, self.ui.customize_button)

        if coordinates is not None:
            coordinates_length = len(coordinates)
            
            if self.mode == "multiple_routes":
                if coordinates_length > 9:
                    self.error_window = ErrorWindow()
                    self.error_window.set_text("The application does not support more than 9 routes.")
                    self.error_window.show()
                    self.ui.customize_button.setEnabled(True)
                else:
                    self.customization_window = CustomizationWindow(self.ui.customize_button, 
                                                                coordinates_length, self.mode)
                    self.customization_window.show()
                
            if self.mode == "one_route":
                self.customization_window = CustomizationWindow(self.ui.customize_button, 
                                                                coordinates_length, self.mode)
                self.customization_window.show()
                
    @Slot()
    def submit(self):
        self.ui.submit_button.setEnabled(False)

        coordinates = self.ui.coordinates_text.text()

        search_organizations = self.ui.organizations_checkbox.isChecked()
        predict_travel_time = self.ui.travel_time_checkbox.isChecked()
        date_time = None
        if predict_travel_time:
            date_time = str(self.ui.dateTimeEdit.dateTime().toPython())
        
        coordinates = self.convert_string_array(coordinates.strip(), self.mode, self.ui.submit_button)

        if coordinates is not None:
            try:
                with open("map_customization_settings.json", mode="r", encoding="utf-8") as file:
                    settings = json.load(file)
            except:
                self.error_window = ErrorWindow()
                self.error_window.set_text("The file with customization settings has not been found.\nTry to save customization settings via interface.")
                self.error_window.show()
                self.ui.submit_button.setEnabled(True)
                return
            
            self.result_window = ResultWindow()
            self.result_window.ui.map_information_table.setColumnCount(2)
        
            if self.mode == "multiple_routes":
                if len(coordinates) > 9:
                    self.error_window = ErrorWindow()
                    self.error_window.set_text("The application does not support more than 9 routes.")
                    self.error_window.show()
                    self.ui.submit_button.setEnabled(True)
                    return
                
                else:                  
                    route_colors = list()
                    for button_name in list(settings.keys()):
                        if "route_color_btn" in button_name:
                            route_colors.append(settings[button_name])
                    
                    try:
                        map_info = draw_area_map_route_multiple(coordinates, bgcolor=settings["background_color_btn"], edge_color=settings["road_color_btn"], 
                                route_color=route_colors, alpha_route=settings["alpha_route_slider"], 
                                alpha_points=settings["alpha_points_slider"], arrival_point_size=settings["arrival_size_slider"],
                                legend=settings["legend_checkbox"], arrival_point_color=settings["arrival_color_btn"], 
                                departure_point_color=settings["departure_color_btn"], departure_point_size=settings["departure_size_slider"], 
                                title=settings["title_line"], title_fontsize=settings["font_size_slider"],
                                place_intermediate_points=settings["intermediate_points_checkbox"], 
                                intermediate_point_color=settings["intermediate_color_btn"], 
                                intermediate_point_size=settings["intermediate_size_slider"])
                    except Exception as e:
                        print(e)
                        self.error_window = ErrorWindow()
                        self.error_window.set_text("An error occurred during drawing the map.\nTry to change coordinates.")
                        self.error_window.show()
                        self.ui.submit_button.setEnabled(True)
                        return

                    row_count = len(map_info['distances_km'])
                    self.result_window.ui.map_information_table.setRowCount(row_count)
                    
                    for i in range(len(map_info['distances_km'])-1, -1, -1):
                        self.result_window.ui.map_information_table.setItem(row_count-i-1, 0, QTableWidgetItem(f"Distance (route {row_count-i})"))
                        self.result_window.ui.map_information_table.setItem(row_count-i-1, 1, QTableWidgetItem(f"{map_info['distances_km'][row_count-i-1]} km"))

                    row_size = self.result_window.ui.map_information_table.verticalHeader().defaultSectionSize() + 0.4
                    self.result_window.ui.map_information_table.setMinimumHeight(round(row_count * row_size))
                    self.result_window.ui.map_information_table.setMaximumHeight(round(row_count * row_size))

                    self.result_window.set_image(map_info['map_image'])
                    self.result_windows_list.append(self.result_window)
                    self.result_windows_list[-1].show()
                    
                          
            if self.mode == "one_route":
                self.result_window.ui.map_information_table.setColumnCount(2)
                
                try:
                    map_info = draw_area_map_route_precise(coordinates, bgcolor=settings["background_color_btn"], edge_color=settings["road_color_btn"], 
                            route_color=settings["route_color_btn"], alpha_route=settings["alpha_route_slider"], 
                            alpha_points=settings["alpha_points_slider"], arrival_point_size=settings["arrival_size_slider"],
                            legend=settings["legend_checkbox"], arrival_point_color=settings["arrival_color_btn"], 
                            departure_point_color=settings["departure_color_btn"], departure_point_size=settings["departure_size_slider"], 
                            title=settings["title_line"], title_fontsize=settings["font_size_slider"],
                            place_intermediate_points=settings["intermediate_points_checkbox"], 
                            intermediate_point_color=settings["intermediate_color_btn"], 
                            intermediate_point_size=settings["intermediate_size_slider"])
                except Exception as e:
                    print(e)
                    self.error_window = ErrorWindow()
                    self.error_window.set_text("An error occurred during drawing the map.\nTry to change coordinates.")
                    self.error_window.show()
                    self.ui.submit_button.setEnabled(True)
                    return
                
                row_count = 1
                self.result_window.ui.map_information_table.setRowCount(row_count)

                if search_organizations:
                    try:
                        organizations_data = classify_points(coordinates[::len(coordinates)-1], dist=map_info['distance_km']*1000)
                        organizations_data_names = list(organizations_data.keys())
                        organizations_data_names.reverse()
                        row_count += len(organizations_data_names)
                        self.result_window.ui.map_information_table.setRowCount(row_count)

                        for i in range(len(organizations_data_names)-1, -1, -1):
                            self.result_window.ui.map_information_table.setItem(row_count-i-1, 0, QTableWidgetItem(organizations_data_names[i].capitalize()))
                            if organizations_data[organizations_data_names[i]][0] == "Residential unit":
                                self.result_window.ui.map_information_table.setItem(row_count-i-1, 1, QTableWidgetItem(organizations_data[organizations_data_names[i]][0]))
                            else:
                                self.result_window.ui.map_information_table.setItem(row_count-i-1, 1, QTableWidgetItem(f"{(", ").join(organizations_data[organizations_data_names[i]])} m"))

                    except Exception as e:
                        print(e)
                        self.error_window = ErrorWindow()
                        self.error_window.set_text("An error occurred while searching for organizations.\nTry to change coordinates.")
                        self.error_window.show()
                        
                if predict_travel_time:
                    try:
                        travel_time_data = predict_traveled_time(coordinates[::len(coordinates)-1], map_info['distance_km'], 
                                                                date_time=date_time, calculate_distance=False)
                        travel_time_data_names = list(travel_time_data.keys())
                        travel_time_data_names.reverse()
                        units = ['', '', 'minutes', 'mm', 'km/h', '°C', '']
                        row_count += len(travel_time_data_names)
                        self.result_window.ui.map_information_table.setRowCount(row_count)

                        for i in range(len(travel_time_data_names)-1, -1, -1):
                            self.result_window.ui.map_information_table.setItem(row_count-i-1, 0, QTableWidgetItem(travel_time_data_names[i].capitalize().replace("_", " ")))
                            self.result_window.ui.map_information_table.setItem(row_count-i-1, 1, QTableWidgetItem(f"{travel_time_data[travel_time_data_names[i]]} {units[i]}"))
                    
                    except Exception as e:
                        print(e)
                        self.error_window = ErrorWindow()
                        self.error_window.set_text("An error occurred while predicting travel time.\nTry to change departure time or coordinates.")
                        self.error_window.show()
                
                self.result_window.ui.map_information_table.setItem(0, 0, QTableWidgetItem("Distance"))
                self.result_window.ui.map_information_table.setItem(0, 1, QTableWidgetItem(f"{map_info['distance_km']} km"))
                self.result_window.set_image(map_info['map_image'])
                self.result_windows_list.append(self.result_window)
            
        row_size = self.result_window.ui.map_information_table.verticalHeader().defaultSectionSize() + 1
        self.result_window.ui.map_information_table.setMinimumHeight(round(row_count * row_size))
        self.result_window.ui.map_information_table.setMaximumHeight(round(row_count * row_size))
        self.result_windows_list[-1].show()
        
        self.ui.submit_button.setEnabled(True)
    
    def convert_string_array(self, string_array, mode, button=None):
        try:
            array = ast.literal_eval(string_array)
            
            if (type(array) is not list) and (type(array) is not tuple):
                raise SyntaxError()
            
            if mode == "one_route":
                for element in array:
                    if (type(element) is not list) and (type(element) is not tuple):
                        raise SyntaxError()
                    if len(element) != 2:
                        raise ValueError()
                    for value in element:
                        if (type(value) is not int) and (type(value) is not float):
                            raise SyntaxError()
            
            if mode == "multiple_routes":
                for item in array:
                    if (type(item) is not list) and (type(item) is not tuple):
                            raise SyntaxError()
                    for element in item:
                        if (type(element) is not list) and (type(element) is not tuple):
                            raise SyntaxError()
                        if len(element) != 2:
                            raise ValueError()
                        for value in element:
                            if (type(value) is not int) and (type(value) is not float):
                                raise SyntaxError()
            return array
    
        except Exception as e:
            print(e)
            self.error_window = ErrorWindow()
            self.error_window.set_text("Input coordinates are incorrect or missing.\nCheck all the brackets and parentheses and try again.")
            self.error_window.show()
            if button is not None:
                button.setEnabled(True)
            return None

class CustomizationWindow(QWidget):
    def __init__(self, open_button, coordinates_length, mode):
        super(CustomizationWindow, self).__init__()
        self.ui = Ui_Customization()
        self.ui.setupUi(self)
        self.open_button = open_button

        self.default_map_customization_settings = {
            "background_color_btn": "white",
            "road_color_btn": "gray",
            "route_color_btn": "#D4AC0D",
            "departure_color_btn": "#CB4335",
            "intermediate_color_btn": "#D4AC0D",
            "arrival_color_btn": "#28B463",
            "alpha_route_slider": 0.8,
            "departure_size_slider": 70, 
            "intermediate_size_slider": 70,
            "arrival_size_slider": 70,
            "title_line": "", 
            "font_size_slider": 15, 
            "alpha_points_slider": 0.8,
            "intermediate_points_checkbox": True,
            "legend_checkbox": True
        }
        
        if os.path.isfile("map_customization_settings.json"):
            with open("map_customization_settings.json", "r", encoding="utf-8") as file:
                self.map_customization_settings = json.load(file)
        else:
            self.error_window = ErrorWindow()
            self.error_window.set_text("The file with customization settings has not been found.\nRestoring default settings.")
            self.error_window.show()
            self.map_customization_settings = self.default_map_customization_settings
            with open("map_customization_settings.json", "w", encoding="utf-8") as file:
                json.dump(self.default_map_customization_settings, file)

        for i in range(1, 10):
            self.default_map_customization_settings[f"route_color_btn_{i}"] = self.default_map_customization_settings["route_color_btn"]
        
        self.name_buttons = {
            "background_color_btn": self.ui.background_color_btn, 
            "road_color_btn": self.ui.road_color_btn, 
            "route_color_btn": self.ui.route_color_btn,
            "departure_color_btn": self.ui.departure_color_btn, 
            "intermediate_color_btn": self.ui.intermediate_color_btn, 
            "arrival_color_btn": self.ui.arrival_color_btn
        }
        
        self.temp_settings = {
            "background_color_btn": self.map_customization_settings["background_color_btn"], 
            "road_color_btn": self.map_customization_settings["road_color_btn"], 
            "route_color_btn": self.map_customization_settings["route_color_btn"],
            "departure_color_btn":self.map_customization_settings["departure_color_btn"], 
            "intermediate_color_btn": self.map_customization_settings["intermediate_color_btn"], 
            "arrival_color_btn": self.map_customization_settings["arrival_color_btn"],
            "alpha_route_slider": self.map_customization_settings["alpha_route_slider"], 
            "departure_size_slider": self.map_customization_settings["departure_size_slider"], 
            "intermediate_size_slider": self.map_customization_settings["intermediate_size_slider"],
            "arrival_size_slider": self.map_customization_settings["arrival_size_slider"], 
            "font_size_slider": self.map_customization_settings["font_size_slider"], 
            "title_line": self.map_customization_settings["title_line"],
            "alpha_points_slider": self.map_customization_settings["alpha_points_slider"],
            "intermediate_points_checkbox": self.map_customization_settings["intermediate_points_checkbox"],
            "legend_checkbox": self.map_customization_settings["legend_checkbox"]
        }
        for i in range(1, 10):
            if self.map_customization_settings.get(f"route_color_btn_{i}"):
                self.temp_settings[f"route_color_btn_{i}"] = self.map_customization_settings[f"route_color_btn_{i}"]
            else:
                self.temp_settings[f"route_color_btn_{i}"] = self.map_customization_settings[f"route_color_btn"]
                self.map_customization_settings[f"route_color_btn_{i}"] = self.map_customization_settings[f"route_color_btn"]
                
        self.name_slider = {
            "alpha_route_slider": self.ui.alpha_route_slider, 
            "departure_size_slider": self.ui.departure_size_slider, 
            "intermediate_size_slider": self.ui.intermediate_size_slider,
            "arrival_size_slider": self.ui.arrival_size_slider, 
            "font_size_slider": self.ui.font_size_slider, 
            "alpha_points_slider": self.ui.alpha_points_slider
        }
        
        self.name_checkbox = {
            "intermediate_points_checkbox": self.ui.intermediate_points_checkbox,
            "legend_checkbox": self.ui.legend_checkbox
        }

        self.ui.restore_defaults_btn.clicked.connect(lambda: self.restore_defaults(self.map_customization_settings))
        self.ui.restore_defaults_btn.click()
        
        if mode == "multiple_routes":           
            count = 0
            for i in range(3):
                for j in range(3):
                    if count == coordinates_length:
                        break
                    count += 1
                    if (i == 0) and (j == 0):
                        continue
                    name = f"route_color_btn_{count}"
                    
                    if self.temp_settings.get(name):
                        color = self.temp_settings[name]
                    elif not self.temp_settings.get(name):
                        color = self.temp_settings["route_color_btn"]
                        self.temp_settings[name] = color
                        
                    if not self.name_buttons.get(name):
                        new_button = QPushButton(text="")
                        new_button.setObjectName(name)
                        self.name_buttons[name] = new_button
                    
                    self.ui.route_btns_layout.addWidget(self.name_buttons[name], i, j)

        for button_name in self.name_buttons.keys():
            self.name_buttons[button_name].setStyleSheet("QPushButton" + " {background-color : " + self.map_customization_settings[button_name] + ";}")
            self.name_buttons[button_name].clicked.connect(self.color_selection)

        for slider_name in self.name_slider.keys():
            self.name_slider[slider_name].valueChanged.connect(self.set_slider_value)
            if "alpha" not in slider_name:
                self.name_slider[slider_name].setValue(self.map_customization_settings[slider_name])
            else:
                self.name_slider[slider_name].setValue(self.map_customization_settings[slider_name] * 100)
        
        for checkbox_name in self.name_checkbox.keys():
            self.name_checkbox[checkbox_name].clicked.connect(self.checkbox_change_status)
        
        self.ui.title_line.textChanged.connect(self.textline_change_status)
                
        self.ui.restore_defaults_btn.clicked.connect(lambda: self.restore_defaults(self.default_map_customization_settings))
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.show_example_btn.clicked.connect(lambda: self.show_example(mode))

    def closeEvent(self, event):
        self.open_button.setEnabled(True)

    @Slot()
    def color_selection(self):
        button = self.sender()
        button_name = button.objectName()
        
        dialog = QColorDialog()
        dialog.setCurrentColor(self.temp_settings[button_name])
        
        if dialog.exec_() == QDialog.Accepted:
            try:
                color = dialog.selectedColor()
                if color.isValid():
                    button.setStyleSheet("QPushButton" + " {background-color : " + color.name() + ";}")
                    self.temp_settings[button_name] = color.name()
            except: 
                pass
    
    @Slot()
    def set_slider_value(self, value):
        slider = self.sender()
        
        label_name = "_".join(slider.objectName().split("_")[:-1:]) + "_label"
        label = slider.parent().findChild(QLabel, label_name)
        
        if "alpha" not in label_name:
            label.setText(str(value))
            self.temp_settings[slider.objectName()] = value
        else: 
            label.setText(str(value / 100))
            self.temp_settings[slider.objectName()] = value / 100
    
    @Slot()
    def checkbox_change_status(self):
        checkbox = self.sender()
        self.temp_settings[checkbox.objectName()] = checkbox.isChecked()
    
    @Slot()
    def textline_change_status(self):
        textline = self.sender()
        self.temp_settings[textline.objectName()] = textline.text()
    
    @Slot()
    def restore_defaults(self, settings):
        for button_name in self.name_buttons.keys():
            self.name_buttons[button_name].setStyleSheet("QPushButton" + " {background-color : " + settings[button_name] + ";}")
            self.temp_settings[button_name] = settings[button_name]
        
        for slider_name in self.name_slider.keys():
            label_name = "_".join(self.name_slider[slider_name].objectName().split("_")[:-1:]) + "_label"
            label = self.name_slider[slider_name].parent().findChild(QLabel, label_name)
            label.setText(str(settings[slider_name]))
            
            self.temp_settings[slider_name] = settings[slider_name]
            
            if "alpha" not in slider_name:
                self.name_slider[slider_name].setValue(settings[slider_name])
                
            else:
                self.name_slider[slider_name].setValue(settings[slider_name] * 100)
        
        for checkbox_name in self.name_checkbox.keys():
            self.name_checkbox[checkbox_name].setChecked(settings[checkbox_name])
            self.temp_settings[checkbox_name] = settings[checkbox_name]
        
        self.ui.title_line.setText(settings["title_line"])
        self.temp_settings["title_line"] = settings["title_line"]
    
    @Slot()
    def save(self):
        self.ui.save_btn.setEnabled(False)
        with open("map_customization_settings.json", mode='w', encoding="utf-8") as file:
            json.dump(self.temp_settings, file)
        self.ui.save_btn.setEnabled(True)
    
    @Slot()
    def show_example(self, mode):
        self.ui.show_example_btn.setEnabled(False)
        if mode == "one_route":
            example_coordinates = [(64.09387193974679, -21.895229437093352), 
                                   (64.09415321474977, -21.89468195069404), 
                                   (64.09463249490439, -21.89662765515066)]
        
            
            draw_area_map_route_precise(example_coordinates, dist=170, filename="example_map", set_file_id=False, middle_point=(64.09412438067676, -21.89607205668655),
                            bgcolor=self.temp_settings["background_color_btn"], edge_color=self.temp_settings["road_color_btn"], 
                            route_color=self.temp_settings["route_color_btn"], alpha_route=self.temp_settings["alpha_route_slider"], 
                            alpha_points=self.temp_settings["alpha_points_slider"], arrival_point_size=self.temp_settings["arrival_size_slider"],
                            legend=self.temp_settings["legend_checkbox"], arrival_point_color=self.temp_settings["arrival_color_btn"], 
                            departure_point_color=self.temp_settings["departure_color_btn"], departure_point_size=self.temp_settings["departure_size_slider"], 
                            title=self.temp_settings["title_line"], title_fontsize=self.temp_settings["font_size_slider"],
                            place_intermediate_points=self.temp_settings["intermediate_points_checkbox"], 
                            intermediate_point_color=self.temp_settings["intermediate_color_btn"], 
                            intermediate_point_size=self.temp_settings["intermediate_size_slider"])
        
        if mode == "multiple_routes":
            example_coordinates = [[(64.09387193974679, -21.895229437093352), (64.09415321474977, -21.89468195069404), (64.09463249490439, -21.89662765515066)], 
                                   [(64.0935730788915, -21.895714798999126), (64.09367724652493, -21.895334456920917)]]
            
            route_colors = list()
            for button_name in list(self.temp_settings.keys()):
                if "route_color_btn" in button_name:
                    route_colors.append(self.temp_settings[button_name])
            
            draw_area_map_route_multiple(example_coordinates, dist=170, filename="example_map", set_file_id=False, middle_point=(64.09412438067676, -21.89607205668655),
                        bgcolor=self.temp_settings["background_color_btn"], edge_color=self.temp_settings["road_color_btn"], 
                        route_color=route_colors, alpha_route=self.temp_settings["alpha_route_slider"], 
                        alpha_points=self.temp_settings["alpha_points_slider"], arrival_point_size=self.temp_settings["arrival_size_slider"],
                        legend=self.temp_settings["legend_checkbox"], arrival_point_color=self.temp_settings["arrival_color_btn"], 
                        departure_point_color=self.temp_settings["departure_color_btn"], departure_point_size=self.temp_settings["departure_size_slider"], 
                        title=self.temp_settings["title_line"], title_fontsize=self.temp_settings["font_size_slider"],
                        place_intermediate_points=self.temp_settings["intermediate_points_checkbox"], 
                        intermediate_point_color=self.temp_settings["intermediate_color_btn"], 
                        intermediate_point_size=self.temp_settings["intermediate_size_slider"])
                    
        path_to_image = "maps/example_map.png"
        scene = QGraphicsScene()
        pixmap = QPixmap(path_to_image)
        pixmap_cropped = pixmap.copy(220, 0, pixmap.width(), pixmap.height()-200)
        scene.addPixmap(pixmap_cropped)
        self.ui.example_map_view.setScene(scene)
        
        self.ui.show_example_btn.setEnabled(True)

class ResultWindow(QWidget):
    def __init__(self):
        super(ResultWindow, self).__init__()
        self.ui = Ui_Result()
        self.ui.setupUi(self)
    
    def set_image(self, path_to_image=None):
        scene = QGraphicsScene()

        pixmap = QPixmap(path_to_image)
        scene.addPixmap(pixmap)

        self.ui.MapImage.setScene(scene)

class TooltipWindow(QWidget):
    def __init__(self, open_button):
        super(TooltipWindow, self).__init__()
        self.ui = Ui_Tooltip()
        self.ui.setupUi(self)
        
        self.open_button = open_button
        
    def closeEvent(self, event):
        self.open_button.setEnabled(True)

class ErrorWindow(QWidget):
    def __init__(self):
        super(ErrorWindow, self).__init__()
        self.ui = Ui_Error()
        self.ui.setupUi(self)

        self.ui.OKButton.clicked.connect(self.closeWindow)
    
    def set_text(self, text):
        self.ui.ErrorMessage.setText(text)

    @Slot()
    def closeWindow(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())