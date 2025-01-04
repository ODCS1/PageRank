from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QVBoxLayout
from PySide6.QtGui import QIcon, QPainter, QColor
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QCategoryAxis, QValueAxis
from random import randint
import sys
from pagerank import crawl, sample_pagerank, iterate_pagerank, DAMPING, SAMPLES
from screen_main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PageRank")
        appIcon = QIcon(':saving/assets/images/pageRank-icon.png')
        self.setWindowIcon(appIcon)

        ######################################################################
        # PUT SHADOWS IN CONTAINERS
        self.put_shadow_elements()
        ######################################################################

        ######################################################################
        # TAB WIDGET FOR GRAPHS
        self.curr_widget_iterate = None
        self.layout_iterate = QVBoxLayout(self.tab_iterate_page_rank)
        self.curr_widget_sample = None
        self.layout_sample = QVBoxLayout(self.tab_sample_page_rank)
        self.curr_widget_links_quantity = None
        self.layout_link_quantity = QVBoxLayout(self.tab_links_quantity_page_rank)
        self.curr_widget_results_comparison = None
        self.layout_results_comparison = QVBoxLayout(self.tab_comparison_results_professor)

        self.correct_results_sample_corpus0 = [0.2223, 0.4303, 0.2145, 0.1329]
        self.correct_results_iterate_corpus0 = [0.2202, 0.4289, 0.2202, 0.1307]
        self.sample_accurancy = 0.0
        self.iterate_accurancy = 0.0
        self.calculate_accurancy()
        self.pagerank_sample_results = {}
        self.pagerank_iterate_results = {}
        self.customize_tab_widget()
        ######################################################################

        ######################################################################
        # SAVE CURRENT DIRECTORY
        self.directory_base = "./pages/corpus"
        self.current_directory = self.directory_base
        ######################################################################

        ######################################################################
        # RIGHT CONTAINER BUTTONS
        self.btn_data.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_data))
        self.btn_graphics.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_graphics))
        self.btn_about.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_about))
        ######################################################################

        ######################################################################
        # COMBO BOX SELECTION ITEM
        self.cbx_option.currentIndexChanged.connect(self.verify_new_value_chx)
        self.cbx_option.setStyleSheet("""
            QComboBox {
                border: 1px solid black;
                padding: 5px; 
                color: rgb(0, 0, 0);
            }
            QComboBox QAbstractItemView {
                border: 1px solid black;
                selection-background-color: lightgray;
                selection-color: black;
                background-color: white;
                color: black;
                outline: none;
            }
        """)
        ######################################################################

    ######################################################################
    # STYLE CUSTOMIZATION
    def put_shadow_elements(self):
        shadow_elements = {
            "frame_header",
            "frame_right",
            "Pages"
        }

        for x in shadow_elements:
            effect = QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self, x).setGraphicsEffect(effect)

    def customize_tab_widget(self):

        self.tabWidget.setStyleSheet("""
            QTabBar {
                background-color: rgb(30, 30, 30);
                border: none;
            }
            QTabBar::tab {
                background: rgb(30, 30, 30);
                color: white;
                padding: 7px;
                margin: 0px 2px;
            }
            QTabBar::tab:selected {
                background: rgb(70, 70, 70);
                border-bottom: 3px solid blue;
            }
            QTabBar::tab:hover {
                background: rgb(60, 60, 60);
            }
            QTabBar::tab:pressed {
                background: rgb(90, 90, 90);
            }
            QTabWidget::pane {
                border: 1px solid black;
            }
        """)


        self.tabWidget.setContentsMargins(5, 5, 5, 5)
    ######################################################################


    ######################################################################
    # GRAPHS
    
    def create_graphs_widget(self):
        self.create_sample_graph()
        self.create_iterate_graph()
        self.create_links_quantity_graph()
        self.create_comparison_graph()

    def create_sample_graph(self):

        self.pagerank_sample_results = sample_pagerank(crawl(self.current_directory), DAMPING, SAMPLES)


        bar_series = QBarSeries()
        categories = []

        # ADDING PAGE RANK VALUES AND CREATING BAR CHARTS FOR EACH FILE
        for key, value in self.pagerank_sample_results.items():
            bar_set = QBarSet(key)
            bar_set.append(value)
            if (self.current_directory == "./pages/corpus2"):
                bar_set.setColor(QColor(randint(10, 255), randint(10, 255), randint(10, 255)))
            bar_series.append(bar_set)
            categories.append(key)

        # CREATING CHART
        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle("PageRank Sample Comparison")

        
        axis_x = QCategoryAxis()
        for i, category in enumerate(categories):
            axis_x.append(category, i)

        chart.addAxis(axis_x, Qt.AlignBottom)
        bar_series.attachAxis(axis_x)


        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)


        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)


        if self.curr_widget_sample is not None:
            self.layout_sample.replaceWidget(self.curr_widget_sample, chart_view)
            self.curr_widget_sample.deleteLater()
        else:
            self.layout_sample.addWidget(chart_view)

        self.curr_widget_sample = chart_view


        chart.createDefaultAxes()


    def create_iterate_graph(self):

        self.pagerank_iterate_results = iterate_pagerank(crawl(self.current_directory), DAMPING)


        bar_series = QBarSeries()
        categories = []


        for key, value in self.pagerank_iterate_results.items():
            bar_set = QBarSet(key)
            bar_set.append(value)
            if (self.current_directory == "./pages/corpus2"):
                bar_set.setColor(QColor(randint(10, 255), randint(10, 255), randint(10, 255)))
            bar_series.append(bar_set)
            categories.append(key)


        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle("PageRank Iteration Comparison")


        axis_x = QCategoryAxis()
        for i, category in enumerate(categories):
            axis_x.append(category, i)

        chart.addAxis(axis_x, Qt.AlignBottom)
        bar_series.attachAxis(axis_x)


        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)


        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)


        if self.curr_widget_iterate is not None:
            self.layout_iterate.replaceWidget(self.curr_widget_iterate, chart_view)
            self.curr_widget_iterate.deleteLater()
        else:
            self.layout_iterate.addWidget(chart_view)

        self.curr_widget_iterate = chart_view


        chart.createDefaultAxes()


    def create_links_quantity_graph(self):

        site_file_crawl_dict = crawl(self.current_directory)

        links_quantity = {key: len(values) for key, values in site_file_crawl_dict.items()}


        bar_series = QBarSeries()
        categories = []


        for key, value in links_quantity.items():
            bar_set = QBarSet(key)
            bar_set.append(value)
            if (self.current_directory == "./pages/corpus2"):
                bar_set.setColor(QColor(randint(10, 255), randint(10, 255), randint(10, 255)))
            bar_series.append(bar_set)
            categories.append(key)


        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle("Links Count Per Page")


        axis_x = QCategoryAxis()
        for i, category in enumerate(categories):
            axis_x.append(category, i)

        chart.addAxis(axis_x, Qt.AlignBottom)
        bar_series.attachAxis(axis_x)


        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)


        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)


        if self.curr_widget_links_quantity is not None:
            self.layout_link_quantity.replaceWidget(self.curr_widget_links_quantity, chart_view)
            self.curr_widget_links_quantity.deleteLater()
        else:
            self.layout_link_quantity.addWidget(chart_view)

        self.curr_widget_links_quantity = chart_view


        chart.createDefaultAxes()


    
    
    def create_comparison_graph(self):

        values_sample = [self.sample_accurancy]
        values_iterate = [self.iterate_accurancy]


        bar_set_sample = QBarSet("Sample PageRank")
        bar_set_sample.append(values_sample)
        bar_set_sample.setColor(QColor(0, 128, 255))

        bar_set_iterate = QBarSet("Iterate PageRank")
        bar_set_iterate.append(values_iterate)
        bar_set_iterate.setColor(QColor(255, 165, 0))


        bar_series = QBarSeries()
        bar_series.append(bar_set_sample)
        bar_series.append(bar_set_iterate)


        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle("Code Accuracy Comparison")


        axis_y = QValueAxis()
        axis_y.setRange(0, 1)
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%.2f")


        chart.addAxis(axis_y, Qt.AlignLeft)
        bar_series.attachAxis(axis_y)


        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        if self.curr_widget_results_comparison is not None:
            self.layout_results_comparison.replaceWidget(self.curr_widget_results_comparison, chart_view)
            self.curr_widget_results_comparison.deleteLater()
        else:
            self.layout_results_comparison.addWidget(chart_view)

        self.curr_widget_results_comparison = chart_view




    def calculate_accurancy(self):

        sample_values = list(sample_pagerank(crawl("./pages/corpus0"), DAMPING, SAMPLES).values())
        iterate_values = list(iterate_pagerank(crawl("./pages/corpus0"), DAMPING).values())
        

        porcent_sample_elements = [0.0 for _ in range(len(sample_values))]
        porcent_iterate_elements = [0.0 for _ in range(len(sample_values))]

        for i in range(len(self.correct_results_sample_corpus0)):
            porcent_sample_elements[i] = self.correct_results_sample_corpus0[i] / sample_values[i]
            porcent_iterate_elements[i] = self.correct_results_iterate_corpus0[i]  / iterate_values[i]
            
        
        self.sample_accurancy =  sum(porcent_sample_elements) / len(porcent_sample_elements)
        self.iterate_accurancy = sum(porcent_iterate_elements) / len(porcent_iterate_elements)
    ######################################################################


    ######################################################################
    # GETTING crawl, sample and iterate FROM pagerank.py
    def get_crawl_page_rank(self) -> None:
        site_file_crawl_dict = crawl(self.current_directory)
        site_file_name = list(site_file_crawl_dict.keys())

        name_display = ""
        for name in site_file_name:
            name_display += name + "\n"
        
        self.lbl_files_name.setText(name_display)
        self.lbl_files_name.setAlignment(Qt.AlignCenter)

        links_display = ""
        for key, values in site_file_crawl_dict.items():
            links_display += f"<b>{key}:</b> {', '.join(values)}<br>"
        
        self.lbl_links_in_file.setText(f"<div style='text-align: left; margin-left: 30px;'>{links_display}</div>")

    def get_sample_pagerank(self):
        pager_rank_sample_dict = sample_pagerank(crawl(self.current_directory), DAMPING, SAMPLES)
        max_key_length = max(len(key) for key in pager_rank_sample_dict.keys())
        
        rank_display = "<div style='text-align: left; margin: 110px;'>"
        for key, value in pager_rank_sample_dict.items():
            value_str = f"{value:.4f}"
            dashes_count = max_key_length + 8 - len(key) - len(value_str)
            dashes = '-' * dashes_count if dashes_count > 0 else ''
            rank_display += f"<b>{key}</b>{dashes} {value_str}<br>"
        rank_display += "</div>"

        self.lbl_sample_rank.setText(rank_display)

    def get_iterate_pagerank(self):
        pager_rank_iterate_dict = iterate_pagerank(crawl(self.current_directory), DAMPING)
        max_key_length = max(len(key) for key in pager_rank_iterate_dict.keys())
        
        rank_display = "<div style='text-align: left; margin: 110px;'>"
        for key, value in pager_rank_iterate_dict.items():
            value_str = f"{value:.4f}"
            dashes_count = max_key_length + 8 - len(key) - len(value_str)
            dashes = '-' * dashes_count if dashes_count > 0 else ''
            rank_display += f"<b>{key}</b>{dashes} {value_str}<br>"
        rank_display += "</div>"

        self.lbl_iterate_page_rank.setText(rank_display)
    ######################################################################


    ######################################################################
    # ADJUST CONTENT BASED ON USER CBX OPTION
    def set_image_label_background(self):
        self.lbl_files_name.clear()
        self.lbl_links_in_file.clear()
        self.lbl_sample_rank.clear()
        self.lbl_iterate_page_rank.clear()

        self.lbl_files_name.setStyleSheet("""
                background-image: url(:/saving/assets/images/domain-name.png);
                background-repeat: no-repeat;
                background-position: center;
        """)

        self.lbl_links_in_file.setStyleSheet("""
                background-image: url(:/saving/assets/images/link-creation.png);
                background-repeat: no-repeat;
                background-position: center;
        """)

        self.lbl_sample_rank.setStyleSheet("""
                background-image: url(:/saving/assets/images/hierarchy.png);
                background-repeat: no-repeat;
                background-position: center;
        """)

        self.lbl_iterate_page_rank.setStyleSheet("""
                background-image: url(:/saving/assets/images/schema.png);
                background-repeat: no-repeat;
                background-position: center;
        """)

        self.tab_iterate_page_rank.setStyleSheet("""
                border: none;
                background-image: url(:/saving/assets/images/python-logo.png);
                background-repeat: no-repeat;
                background-position: center;
        """)

        self.tab_sample_page_rank.setStyleSheet("""
                border: none;
                background-image: url(:/saving/assets/images/python-logo.png);
                background-repeat: no-repeat;
                background-position: center;
        """)

        self.tab_links_quantity_page_rank.setStyleSheet("""
                border: none;
                background-image: url(:/saving/assets/images/python-logo.png);
                background-repeat: no-repeat;
                background-position: center;
        """)

        self.tab_comparison_results_professor.setStyleSheet("""
                border: none;
                background-image: url(:/saving/assets/images/python-logo.png);
                background-repeat: no-repeat;
                background-position: center;
        """)
        

    def clear_image_and_text_label(self):
        self.lbl_files_name.clear()
        self.lbl_links_in_file.clear()
        self.lbl_sample_rank.clear()
        self.lbl_iterate_page_rank.clear()

        self.lbl_files_name.setStyleSheet("background: none;")
        self.lbl_links_in_file.setStyleSheet("background: none;")
        self.lbl_sample_rank.setStyleSheet("background: none;")
        self.lbl_iterate_page_rank.setStyleSheet("background: none;")
        self.tab_iterate_page_rank.setStyleSheet("border: none; background: none;")
        self.tab_sample_page_rank.setStyleSheet("border: none; background: none;")
        self.tab_links_quantity_page_rank.setStyleSheet("border: none; background: none;")
        self.tab_comparison_results_professor.setStyleSheet("border: none; background: none;")
    

    def clear_graph_layout(self):
        if self.curr_widget_iterate is not None:
            self.layout_iterate.removeWidget(self.curr_widget_iterate)
            self.curr_widget_iterate.deleteLater()
            self.curr_widget_iterate = None

            self.layout_sample.removeWidget(self.curr_widget_sample)
            self.curr_widget_sample.deleteLater()
            self.curr_widget_sample = None

            self.layout_link_quantity.removeWidget(self.curr_widget_links_quantity)
            self.curr_widget_links_quantity.deleteLater()
            self.curr_widget_links_quantity = None


            self.layout_results_comparison.removeWidget(self.curr_widget_results_comparison)
            self.curr_widget_results_comparison.deleteLater()
            self.curr_widget_results_comparison = None

    ######################################################################


    def verify_new_value_chx(self, new_index):

        match new_index:
            case 0:
                self.current_directory = self.directory_base
                self.set_image_label_background()
                self.clear_graph_layout()
                return
            case 1:
                self.current_directory = self.directory_base + "0"
            case 2:
                self.current_directory = self.directory_base + "1"
            case 3:
                self.current_directory = self.directory_base + "2"

        self.clear_image_and_text_label()
        self.get_crawl_page_rank()
        self.get_sample_pagerank()
        self.get_iterate_pagerank()
        self.create_graphs_widget()


if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    aplicacao.exec()
