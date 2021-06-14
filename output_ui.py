# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(952, 672)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(App.sizePolicy().hasHeightForWidth())
        App.setSizePolicy(sizePolicy)
        App.setMinimumSize(QtCore.QSize(952, 672))
        App.setMaximumSize(QtCore.QSize(952, 672))
        App.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(App)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs_area = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs_area.setGeometry(QtCore.QRect(30, 10, 891, 611))
        self.tabs_area.setMovable(False)
        self.tabs_area.setObjectName("tabs_area")
        self.outdoor_models = QtWidgets.QWidget()
        self.outdoor_models.setObjectName("outdoor_models")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.outdoor_models)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 222, 170))
        self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(222, 170))
        self.verticalLayoutWidget.setMaximumSize(QtCore.QSize(222, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.free_space_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.free_space_rb.setMinimumSize(QtCore.QSize(220, 23))
        self.free_space_rb.setMaximumSize(QtCore.QSize(220, 23))
        self.free_space_rb.setChecked(True)
        self.free_space_rb.setObjectName("free_space_rb")
        self.verticalLayout.addWidget(self.free_space_rb)
        self.okumura_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.okumura_rb.setMinimumSize(QtCore.QSize(220, 23))
        self.okumura_rb.setMaximumSize(QtCore.QSize(220, 23))
        self.okumura_rb.setObjectName("okumura_rb")
        self.verticalLayout.addWidget(self.okumura_rb)
        self.ecc_33_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ecc_33_rb.setMinimumSize(QtCore.QSize(220, 23))
        self.ecc_33_rb.setMaximumSize(QtCore.QSize(220, 23))
        self.ecc_33_rb.setObjectName("ecc_33_rb")
        self.verticalLayout.addWidget(self.ecc_33_rb)
        self.cost_231_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cost_231_rb.setMinimumSize(QtCore.QSize(220, 23))
        self.cost_231_rb.setMaximumSize(QtCore.QSize(220, 23))
        self.cost_231_rb.setObjectName("cost_231_rb")
        self.verticalLayout.addWidget(self.cost_231_rb)
        self.two_ray_rb_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.two_ray_rb_2.setMinimumSize(QtCore.QSize(220, 23))
        self.two_ray_rb_2.setMaximumSize(QtCore.QSize(220, 23))
        self.two_ray_rb_2.setObjectName("two_ray_rb_2")
        self.verticalLayout.addWidget(self.two_ray_rb_2)
        self.ericsson_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.ericsson_rb.setMinimumSize(QtCore.QSize(220, 23))
        self.ericsson_rb.setMaximumSize(QtCore.QSize(220, 23))
        self.ericsson_rb.setObjectName("ericsson_rb")
        self.verticalLayout.addWidget(self.ericsson_rb)
        self.graphics_view = PlotWidget(self.outdoor_models)
        self.graphics_view.setGeometry(QtCore.QRect(400, 10, 471, 441))
        self.graphics_view.setMinimumSize(QtCore.QSize(471, 441))
        self.graphics_view.setMaximumSize(QtCore.QSize(471, 441))
        self.graphics_view.setObjectName("graphics_view")
        self.verticalWidget_2 = QtWidgets.QWidget(self.outdoor_models)
        self.verticalWidget_2.setGeometry(QtCore.QRect(250, 380, 141, 170))
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(141, 170))
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(141, 170))
        self.verticalWidget_2.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.metro_rb = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.metro_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.metro_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.metro_rb.setObjectName("metro_rb")
        self.verticalLayout_2.addWidget(self.metro_rb)
        self.urban_rb = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.urban_rb.setEnabled(True)
        self.urban_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.urban_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.urban_rb.setChecked(False)
        self.urban_rb.setObjectName("urban_rb")
        self.verticalLayout_2.addWidget(self.urban_rb)
        self.med_city_rb = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.med_city_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.med_city_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.med_city_rb.setObjectName("med_city_rb")
        self.verticalLayout_2.addWidget(self.med_city_rb)
        self.suburb_rb = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.suburb_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.suburb_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.suburb_rb.setObjectName("suburb_rb")
        self.verticalLayout_2.addWidget(self.suburb_rb)
        self.village_rb = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.village_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.village_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.village_rb.setObjectName("village_rb")
        self.verticalLayout_2.addWidget(self.village_rb)
        self.open_area_rb = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.open_area_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.open_area_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.open_area_rb.setObjectName("open_area_rb")
        self.verticalLayout_2.addWidget(self.open_area_rb)
        self.formLayoutWidget = QtWidgets.QWidget(self.outdoor_models)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 311))
        self.formLayoutWidget.setMinimumSize(QtCore.QSize(361, 311))
        self.formLayoutWidget.setMaximumSize(QtCore.QSize(361, 311))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Loss_exp_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Loss_exp_label.setMinimumSize(QtCore.QSize(141, 25))
        self.Loss_exp_label.setMaximumSize(QtCore.QSize(141, 25))
        self.Loss_exp_label.setObjectName("Loss_exp_label")
        self.gridLayout_2.addWidget(self.Loss_exp_label, 1, 0, 1, 1)
        self.max_meter_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.max_meter_label.setMinimumSize(QtCore.QSize(102, 25))
        self.max_meter_label.setMaximumSize(QtCore.QSize(102, 25))
        self.max_meter_label.setObjectName("max_meter_label")
        self.gridLayout_2.addWidget(self.max_meter_label, 4, 0, 1, 1)
        self.loss_exp_value = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.loss_exp_value.setMinimumSize(QtCore.QSize(179, 25))
        self.loss_exp_value.setMaximumSize(QtCore.QSize(179, 25))
        self.loss_exp_value.setStyleSheet("border-color: rgb(52, 101, 164);")
        self.loss_exp_value.setObjectName("loss_exp_value")
        self.gridLayout_2.addWidget(self.loss_exp_value, 1, 1, 1, 1)
        self.receiver_height_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.receiver_height_label.setMinimumSize(QtCore.QSize(151, 25))
        self.receiver_height_label.setMaximumSize(QtCore.QSize(151, 25))
        self.receiver_height_label.setObjectName("receiver_height_label")
        self.gridLayout_2.addWidget(self.receiver_height_label, 3, 0, 1, 1)
        self.receiver_height = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.receiver_height.setMinimumSize(QtCore.QSize(179, 25))
        self.receiver_height.setMaximumSize(QtCore.QSize(179, 25))
        self.receiver_height.setStyleSheet("border-color: rgb(52, 101, 164);")
        self.receiver_height.setObjectName("receiver_height")
        self.gridLayout_2.addWidget(self.receiver_height, 3, 1, 1, 1)
        self.freq_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.freq_label.setMinimumSize(QtCore.QSize(103, 25))
        self.freq_label.setMaximumSize(QtCore.QSize(103, 25))
        self.freq_label.setObjectName("freq_label")
        self.gridLayout_2.addWidget(self.freq_label, 0, 0, 1, 1)
        self.transmitter_height = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.transmitter_height.setMinimumSize(QtCore.QSize(179, 25))
        self.transmitter_height.setMaximumSize(QtCore.QSize(179, 25))
        self.transmitter_height.setStyleSheet("border-color: rgb(52, 101, 164);")
        self.transmitter_height.setObjectName("transmitter_height")
        self.gridLayout_2.addWidget(self.transmitter_height, 2, 1, 1, 1)
        self.frequency_outdoor = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.frequency_outdoor.setMinimumSize(QtCore.QSize(179, 25))
        self.frequency_outdoor.setMaximumSize(QtCore.QSize(179, 25))
        self.frequency_outdoor.setStyleSheet("border-color: rgb(52, 101, 164);")
        self.frequency_outdoor.setObjectName("frequency_outdoor")
        self.gridLayout_2.addWidget(self.frequency_outdoor, 0, 1, 1, 1)
        self.trans_height_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.trans_height_label.setMinimumSize(QtCore.QSize(172, 25))
        self.trans_height_label.setMaximumSize(QtCore.QSize(172, 25))
        self.trans_height_label.setObjectName("trans_height_label")
        self.gridLayout_2.addWidget(self.trans_height_label, 2, 0, 1, 1)
        self.distance_max_meter = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.distance_max_meter.setMinimumSize(QtCore.QSize(179, 25))
        self.distance_max_meter.setMaximumSize(QtCore.QSize(179, 25))
        self.distance_max_meter.setStyleSheet("border-color: rgb(52, 101, 164);")
        self.distance_max_meter.setObjectName("distance_max_meter")
        self.gridLayout_2.addWidget(self.distance_max_meter, 4, 1, 1, 1)
        self.correction_factor_label = QtWidgets.QLabel(self.outdoor_models)
        self.correction_factor_label.setGeometry(QtCore.QRect(250, 340, 141, 31))
        self.correction_factor_label.setMinimumSize(QtCore.QSize(141, 31))
        self.correction_factor_label.setMaximumSize(QtCore.QSize(141, 31))
        self.correction_factor_label.setWordWrap(True)
        self.correction_factor_label.setObjectName("correction_factor_label")
        self.prop_model_label = QtWidgets.QLabel(self.outdoor_models)
        self.prop_model_label.setGeometry(QtCore.QRect(10, 340, 141, 25))
        self.prop_model_label.setMinimumSize(QtCore.QSize(141, 25))
        self.prop_model_label.setMaximumSize(QtCore.QSize(141, 25))
        self.prop_model_label.setObjectName("prop_model_label")
        self.calc_outdoor_btn = QtWidgets.QPushButton(self.outdoor_models)
        self.calc_outdoor_btn.setEnabled(True)
        self.calc_outdoor_btn.setGeometry(QtCore.QRect(460, 480, 359, 25))
        self.calc_outdoor_btn.setMinimumSize(QtCore.QSize(359, 25))
        self.calc_outdoor_btn.setMaximumSize(QtCore.QSize(359, 25))
        self.calc_outdoor_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.calc_outdoor_btn.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.calc_outdoor_btn.setObjectName("calc_outdoor_btn")
        self.tabs_area.addTab(self.outdoor_models, "")
        self.indoor_models = QtWidgets.QWidget()
        self.indoor_models.setObjectName("indoor_models")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.indoor_models)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 370, 222, 170))
        self.verticalLayoutWidget_2.setMinimumSize(QtCore.QSize(222, 170))
        self.verticalLayoutWidget_2.setMaximumSize(QtCore.QSize(222, 170))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.itu_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.itu_rb.setEnabled(True)
        self.itu_rb.setMinimumSize(QtCore.QSize(220, 23))
        self.itu_rb.setMaximumSize(QtCore.QSize(220, 23))
        self.itu_rb.setChecked(True)
        self.itu_rb.setObjectName("itu_rb")
        self.verticalLayout_3.addWidget(self.itu_rb)
        self.log_distance_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.log_distance_rb.setMinimumSize(QtCore.QSize(220, 23))
        self.log_distance_rb.setMaximumSize(QtCore.QSize(220, 23))
        self.log_distance_rb.setObjectName("log_distance_rb")
        self.verticalLayout_3.addWidget(self.log_distance_rb)
        self.calc_indoor_btn = QtWidgets.QPushButton(self.indoor_models)
        self.calc_indoor_btn.setEnabled(True)
        self.calc_indoor_btn.setGeometry(QtCore.QRect(460, 480, 359, 25))
        self.calc_indoor_btn.setMinimumSize(QtCore.QSize(359, 25))
        self.calc_indoor_btn.setMaximumSize(QtCore.QSize(359, 25))
        self.calc_indoor_btn.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.calc_indoor_btn.setObjectName("calc_indoor_btn")
        self.graphics_view_2 = PlotWidget(self.indoor_models)
        self.graphics_view_2.setGeometry(QtCore.QRect(400, 10, 471, 441))
        self.graphics_view_2.setMinimumSize(QtCore.QSize(471, 441))
        self.graphics_view_2.setMaximumSize(QtCore.QSize(471, 441))
        self.graphics_view_2.setObjectName("graphics_view_2")
        self.prop_model_label_2 = QtWidgets.QLabel(self.indoor_models)
        self.prop_model_label_2.setGeometry(QtCore.QRect(10, 340, 141, 25))
        self.prop_model_label_2.setMinimumSize(QtCore.QSize(141, 25))
        self.prop_model_label_2.setMaximumSize(QtCore.QSize(141, 25))
        self.prop_model_label_2.setObjectName("prop_model_label_2")
        self.correction_factor_label_2 = QtWidgets.QLabel(self.indoor_models)
        self.correction_factor_label_2.setGeometry(QtCore.QRect(250, 340, 141, 31))
        self.correction_factor_label_2.setMinimumSize(QtCore.QSize(141, 31))
        self.correction_factor_label_2.setMaximumSize(QtCore.QSize(141, 31))
        self.correction_factor_label_2.setWordWrap(True)
        self.correction_factor_label_2.setObjectName("correction_factor_label_2")
        self.verticalWidget_3 = QtWidgets.QWidget(self.indoor_models)
        self.verticalWidget_3.setGeometry(QtCore.QRect(250, 370, 141, 170))
        self.verticalWidget_3.setMinimumSize(QtCore.QSize(141, 170))
        self.verticalWidget_3.setMaximumSize(QtCore.QSize(141, 170))
        self.verticalWidget_3.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.no_fading_rb = QtWidgets.QRadioButton(self.verticalWidget_3)
        self.no_fading_rb.setEnabled(True)
        self.no_fading_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.no_fading_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.no_fading_rb.setChecked(False)
        self.no_fading_rb.setObjectName("no_fading_rb")
        self.verticalLayout_4.addWidget(self.no_fading_rb)
        self.slow_fading_rb = QtWidgets.QRadioButton(self.verticalWidget_3)
        self.slow_fading_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.slow_fading_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.slow_fading_rb.setObjectName("slow_fading_rb")
        self.verticalLayout_4.addWidget(self.slow_fading_rb)
        self.fast_fading_rb = QtWidgets.QRadioButton(self.verticalWidget_3)
        self.fast_fading_rb.setMinimumSize(QtCore.QSize(139, 18))
        self.fast_fading_rb.setMaximumSize(QtCore.QSize(139, 18))
        self.fast_fading_rb.setObjectName("fast_fading_rb")
        self.verticalLayout_4.addWidget(self.fast_fading_rb)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.indoor_models)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 371, 311))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.frequency_indoor = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.frequency_indoor.setReadOnly(False)
        self.frequency_indoor.setObjectName("frequency_indoor")
        self.gridLayout.addWidget(self.frequency_indoor, 0, 1, 1, 1)
        self.max_distance_value = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.max_distance_value.setReadOnly(False)
        self.max_distance_value.setObjectName("max_distance_value")
        self.gridLayout.addWidget(self.max_distance_value, 1, 1, 1, 1)
        self.floor_number = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.floor_number.setEnabled(False)
        self.floor_number.setReadOnly(False)
        self.floor_number.setObjectName("floor_number")
        self.gridLayout.addWidget(self.floor_number, 8, 1, 1, 1)
        self.frequency_ind_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.frequency_ind_label.setWordWrap(True)
        self.frequency_ind_label.setObjectName("frequency_ind_label")
        self.gridLayout.addWidget(self.frequency_ind_label, 0, 0, 1, 1)
        self.reference_distance_value = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.reference_distance_value.setReadOnly(False)
        self.reference_distance_value.setObjectName("reference_distance_value")
        self.gridLayout.addWidget(self.reference_distance_value, 2, 1, 1, 1)
        self.power_loss_coef_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.power_loss_coef_label.setWordWrap(True)
        self.power_loss_coef_label.setObjectName("power_loss_coef_label")
        self.gridLayout.addWidget(self.power_loss_coef_label, 3, 0, 1, 1)
        self.floor_loss_factor_value = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.floor_loss_factor_value.setObjectName("floor_loss_factor_value")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.addItem("")
        self.floor_loss_factor_value.setItemText(7, "")
        self.gridLayout.addWidget(self.floor_loss_factor_value, 6, 1, 1, 1)
        self.power_loss_value = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.power_loss_value.setObjectName("power_loss_value")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.power_loss_value.addItem("")
        self.gridLayout.addWidget(self.power_loss_value, 3, 1, 1, 1)
        self.num_of_floors_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.num_of_floors_label.setEnabled(False)
        self.num_of_floors_label.setWordWrap(True)
        self.num_of_floors_label.setObjectName("num_of_floors_label")
        self.gridLayout.addWidget(self.num_of_floors_label, 8, 0, 1, 1)
        self.floor_loss_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.floor_loss_label.setWordWrap(True)
        self.floor_loss_label.setObjectName("floor_loss_label")
        self.gridLayout.addWidget(self.floor_loss_label, 6, 0, 1, 1)
        self.ref_dist_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.ref_dist_label.setWordWrap(True)
        self.ref_dist_label.setObjectName("ref_dist_label")
        self.gridLayout.addWidget(self.ref_dist_label, 2, 0, 1, 1)
        self.area_value = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.area_value.setEnabled(False)
        self.area_value.setObjectName("area_value")
        self.area_value.addItem("")
        self.area_value.addItem("")
        self.area_value.addItem("")
        self.gridLayout.addWidget(self.area_value, 9, 1, 1, 1)
        self.max_distance_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.max_distance_label.setWordWrap(True)
        self.max_distance_label.setObjectName("max_distance_label")
        self.gridLayout.addWidget(self.max_distance_label, 1, 0, 1, 1)
        self.area_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.area_label.setEnabled(False)
        self.area_label.setWordWrap(True)
        self.area_label.setObjectName("area_label")
        self.gridLayout.addWidget(self.area_label, 9, 0, 1, 1)
        self.path_loss_exponent = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.path_loss_exponent.setWordWrap(True)
        self.path_loss_exponent.setObjectName("path_loss_exponent")
        self.gridLayout.addWidget(self.path_loss_exponent, 5, 0, 1, 1)
        self.path_loss_exp_value = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.path_loss_exp_value.setObjectName("path_loss_exp_value")
        self.path_loss_exp_value.addItem("")
        self.path_loss_exp_value.addItem("")
        self.path_loss_exp_value.addItem("")
        self.path_loss_exp_value.addItem("")
        self.path_loss_exp_value.addItem("")
        self.path_loss_exp_value.addItem("")
        self.path_loss_exp_value.addItem("")
        self.path_loss_exp_value.addItem("")
        self.gridLayout.addWidget(self.path_loss_exp_value, 5, 1, 1, 1)
        self.tabs_area.addTab(self.indoor_models, "")
        App.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(App)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        App.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)
        self.export_pdf_button = QtWidgets.QAction(App)
        self.export_pdf_button.setObjectName("export_pdf_button")
        self.actionClose = QtWidgets.QAction(App)
        self.actionClose.setObjectName("actionClose")
        self.actionSave_Settings = QtWidgets.QAction(App)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionLoad_Settings = QtWidgets.QAction(App)
        self.actionLoad_Settings.setObjectName("actionLoad_Settings")
        self.actionOkumura_2 = QtWidgets.QAction(App)
        self.actionOkumura_2.setObjectName("actionOkumura_2")
        self.actionFree_Space = QtWidgets.QAction(App)
        self.actionFree_Space.setObjectName("actionFree_Space")
        self.actionAbout = QtWidgets.QAction(App)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(App)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.export_pdf_button)
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(App)
        self.tabs_area.setCurrentIndex(0)
        self.actionClose.triggered.connect(App.close)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Propagation Models Calculator"))
        self.free_space_rb.setText(_translate("App", "Free Space"))
        self.okumura_rb.setText(_translate("App", "Okumura Hata"))
        self.ecc_33_rb.setText(_translate("App", "ECC 33"))
        self.cost_231_rb.setText(_translate("App", "Cost 231"))
        self.two_ray_rb_2.setText(_translate("App", "Two - Ray"))
        self.ericsson_rb.setText(_translate("App", "Ericsson"))
        self.metro_rb.setText(_translate("App", "Metropolitan"))
        self.urban_rb.setText(_translate("App", "Urban"))
        self.med_city_rb.setText(_translate("App", "Medium City"))
        self.suburb_rb.setText(_translate("App", "Sub-Urban"))
        self.village_rb.setText(_translate("App", "Village"))
        self.open_area_rb.setText(_translate("App", "Open Area"))
        self.Loss_exp_label.setText(_translate("App", "   L   (Loss exponent) "))
        self.max_meter_label.setText(_translate("App", "  Max Distance:"))
        self.loss_exp_value.setPlaceholderText(_translate("App", "Value"))
        self.receiver_height_label.setText(_translate("App", "  Reciever Height (Htt)"))
        self.receiver_height.setPlaceholderText(_translate("App", "Meters"))
        self.freq_label.setText(_translate("App", "   Frequency (F)"))
        self.transmitter_height.setPlaceholderText(_translate("App", "Meters"))
        self.frequency_outdoor.setPlaceholderText(_translate("App", "Hz"))
        self.trans_height_label.setText(_translate("App", "  Transmitter Height (Htr)"))
        self.distance_max_meter.setPlaceholderText(_translate("App", "Meters"))
        self.correction_factor_label.setText(_translate("App", "Correction Factor (Ch)"))
        self.prop_model_label.setText(_translate("App", "Propagation Models:"))
        self.calc_outdoor_btn.setText(_translate("App", "Calculate"))
        self.tabs_area.setTabText(self.tabs_area.indexOf(self.outdoor_models), _translate("App", "Outdoor Models"))
        self.itu_rb.setText(_translate("App", "ITU"))
        self.log_distance_rb.setText(_translate("App", "Log Distance"))
        self.calc_indoor_btn.setText(_translate("App", "Calculate"))
        self.prop_model_label_2.setText(_translate("App", "Propagation Models:"))
        self.correction_factor_label_2.setText(_translate("App", "Options:"))
        self.no_fading_rb.setText(_translate("App", "No Fading"))
        self.slow_fading_rb.setText(_translate("App", "Slow Fadding"))
        self.fast_fading_rb.setText(_translate("App", "Fast Fadding"))
        self.frequency_indoor.setPlaceholderText(_translate("App", "Hz"))
        self.max_distance_value.setPlaceholderText(_translate("App", "Meters"))
        self.floor_number.setPlaceholderText(_translate("App", "Floor Number"))
        self.frequency_ind_label.setText(_translate("App", "Frequency (F)"))
        self.reference_distance_value.setPlaceholderText(_translate("App", "Meters"))
        self.power_loss_coef_label.setText(_translate("App", "Distance Power Loss Coefficient"))
        self.floor_loss_factor_value.setItemText(0, _translate("App", "9"))
        self.floor_loss_factor_value.setItemText(1, _translate("App", "19"))
        self.floor_loss_factor_value.setItemText(2, _translate("App", "24"))
        self.floor_loss_factor_value.setItemText(3, _translate("App", "16"))
        self.floor_loss_factor_value.setItemText(4, _translate("App", "22"))
        self.floor_loss_factor_value.setItemText(5, _translate("App", "28"))
        self.floor_loss_factor_value.setItemText(6, _translate("App", "Floor Dependency"))
        self.power_loss_value.setItemText(0, _translate("App", "33"))
        self.power_loss_value.setItemText(1, _translate("App", "32"))
        self.power_loss_value.setItemText(2, _translate("App", "30"))
        self.power_loss_value.setItemText(3, _translate("App", "28"))
        self.power_loss_value.setItemText(4, _translate("App", "31"))
        self.power_loss_value.setItemText(5, _translate("App", "24"))
        self.power_loss_value.setItemText(6, _translate("App", "22"))
        self.power_loss_value.setItemText(7, _translate("App", "20"))
        self.power_loss_value.setItemText(8, _translate("App", "17"))
        self.num_of_floors_label.setText(_translate("App", "Number of floors"))
        self.floor_loss_label.setText(_translate("App", "Floor Penetration Loss Factor"))
        self.ref_dist_label.setText(_translate("App", "Reference Distance"))
        self.area_value.setItemText(0, _translate("App", "Residential"))
        self.area_value.setItemText(1, _translate("App", "Office"))
        self.area_value.setItemText(2, _translate("App", "Commercial"))
        self.max_distance_label.setText(_translate("App", "Max Distance:"))
        self.area_label.setText(_translate("App", "Area"))
        self.path_loss_exponent.setText(_translate("App", "Path loss exponent"))
        self.path_loss_exp_value.setItemText(0, _translate("App", "Infinite Space"))
        self.path_loss_exp_value.setItemText(1, _translate("App", "Retail Store"))
        self.path_loss_exp_value.setItemText(2, _translate("App", "Grocery Store"))
        self.path_loss_exp_value.setItemText(3, _translate("App", "Office"))
        self.path_loss_exp_value.setItemText(4, _translate("App", "Office with Hard Partition"))
        self.path_loss_exp_value.setItemText(5, _translate("App", "Office with Soft Partition"))
        self.path_loss_exp_value.setItemText(6, _translate("App", "Textile or Chemical"))
        self.path_loss_exp_value.setItemText(7, _translate("App", "Commercial"))
        self.tabs_area.setTabText(self.tabs_area.indexOf(self.indoor_models), _translate("App", "Indoor Models"))
        self.menuFile.setTitle(_translate("App", "File"))
        self.menuHelp.setTitle(_translate("App", "Help"))
        self.export_pdf_button.setText(_translate("App", "Export PDF"))
        self.actionClose.setText(_translate("App", "Close"))
        self.actionSave_Settings.setText(_translate("App", "Save Settings"))
        self.actionLoad_Settings.setText(_translate("App", "Load Settings"))
        self.actionOkumura_2.setText(_translate("App", "Okumura"))
        self.actionFree_Space.setText(_translate("App", "Free Space"))
        self.actionAbout.setText(_translate("App", "About"))
        self.actionHelp.setText(_translate("App", "Info (PDF)"))
from pyqtgraph import PlotWidget
