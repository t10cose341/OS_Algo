import sys
import itertools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from utils import *

UI = loadUiType('Scheduler.ui')[0]

class Main(QMainWindow , UI):

    scale = 50.0

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('CPU Scheduler team 10')
        self.setWindowIcon(QtGui.QIcon("CPU2.png"))
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        self.Handle_events()
        self.AutoResize_Tables()
        self.lineEdit_13.setText('   5')

    def Handle_events(self):
        self.pushButton_14.clicked.connect(self.Back)
        self.pushButton_17.clicked.connect(self.Back)
        self.pushButton_20.clicked.connect(self.Back)
        self.pushButton_23.clicked.connect(self.Back)
        self.pushButton_26.clicked.connect(self.Back)
        self.pushButton_29.clicked.connect(self.Back)
        self.pushButton_14.clicked.connect(self.Back)
        self.pushButton_7.clicked.connect(self.Back)
        self.pushButton_11.clicked.connect(self.Back)
        self.pushButton_85.clicked.connect(self.Back)
        self.pushButton_88.clicked.connect(self.Back)
        self.pushButton_3.clicked.connect(self.FCFS_Tab)
        self.pushButton_2.clicked.connect(self.Table_FCFS)
        self.pushButton_4.clicked.connect(self.RR_Choices_Tab)
        self.pushButton_84.clicked.connect(self.RR_Tab)
        self.pushButton_83.clicked.connect(self.Priority_RR_Tab)
        self.pushButton_5.clicked.connect(self.SJF_Choices_Tab)
        self.pushButton_6.clicked.connect(self.Priority_Choices_Tab)
        self.pushButton_13.clicked.connect(self.SJF_Tab)
        self.pushButton_12.clicked.connect(self.SRTF_Tab)
        self.pushButton_22.clicked.connect(self.Priority_Tab)
        self.pushButton_21.clicked.connect(self.Preemptive_Priority_Tab)
        self.pushButton_8.clicked.connect(self.FCFS)
        self.pushButton_15.clicked.connect(self.Table_SJF)
        self.pushButton_16.clicked.connect(self.SJF)
        self.pushButton_24.clicked.connect(self.Table_Priority)
        self.pushButton_25.clicked.connect(self.Priority)
        self.pushButton_9.clicked.connect(self.Table_RR)
        self.pushButton_10.clicked.connect(self.RR)
        self.pushButton_86.clicked.connect(self.Table_Priority_RR)
        self.pushButton_87.clicked.connect(self.Priority_RR)
        self.pushButton_18.clicked.connect(self.Table_SRTF)
        self.pushButton_19.clicked.connect(self.SRTF)
        self.pushButton_32.clicked.connect(self.SRTF_Zoom_In)
        self.pushButton_31.clicked.connect(self.SRTF_Zoom_Out)
        self.pushButton_33.clicked.connect(self.FCFS_Zoom_In)
        self.pushButton_34.clicked.connect(self.FCFS_Zoom_Out)
        self.pushButton_35.clicked.connect(self.RR_Zoom_In)
        self.pushButton_36.clicked.connect(self.RR_Zoom_Out)
        self.pushButton_89.clicked.connect(self.Priority_RR_Zoom_In)
        self.pushButton_90.clicked.connect(self.Priority_RR_Zoom_Out)
        self.pushButton_37.clicked.connect(self.SJF_Zoom_In)
        self.pushButton_38.clicked.connect(self.SJF_Zoom_Out)
        self.pushButton_39.clicked.connect(self.Priority_Zoom_In)
        self.pushButton_40.clicked.connect(self.Priority_Zoom_Out)
        self.pushButton_27.clicked.connect(self.Table_Preemptive_Priority)
        self.pushButton_28.clicked.connect(self.Preemptive_Priority)
        self.pushButton_41.clicked.connect(self.Preemptive_Priority_Zoom_In)
        self.pushButton_42.clicked.connect(self.Preemptive_Priority_Zoom_Out)



    def SRTF_Zoom_In(self):
        Main.scale += 10
        self.SRTF()

    def SRTF_Zoom_Out(self):
        if Main.scale != 10:
            Main.scale -= 10
            self.SRTF()

    def FCFS_Zoom_In(self):
        Main.scale += 10
        self.FCFS()

    def FCFS_Zoom_Out(self):
        if Main.scale != 10:
            Main.scale -= 10
            self.FCFS()

    def RR_Zoom_In(self):
        Main.scale += 10
        self.RR()

    def RR_Zoom_Out(self):
        if Main.scale != 10:
            Main.scale -= 10
            self.RR()

    def Priority_RR_Zoom_In(self):
        Main.scale += 10
        self.Priority_RR()

    def Priority_RR_Zoom_Out(self):
        if Main.scale != 10:
            Main.scale -= 10
            self.Priority_RR()

    def SJF_Zoom_In(self):
        Main.scale += 10
        self.SJF()

    def SJF_Zoom_Out(self):
        if Main.scale != 10:
            Main.scale -= 10
            self.SJF()

    def Priority_Zoom_In(self):
        Main.scale += 10
        self.Priority()

    def Priority_Zoom_Out(self):
        if Main.scale != 10:
            Main.scale -= 10
            self.Priority()

    def Preemptive_Priority_Zoom_In(self):
        Main.scale += 10
        self.Preemptive_Priority()

    def Preemptive_Priority_Zoom_Out(self):
        if Main.scale != 10:
            Main.scale -= 10
            self.Preemptive_Priority()


    def AutoResize_Tables(self):
        header = self.tableWidget_3.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_1 = self.tableWidget_5.horizontalHeader()
        header_1.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_1.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_2 = self.tableWidget_7.horizontalHeader()
        header_2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_3 = self.tableWidget_9.horizontalHeader()
        header_3.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_3.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_3 = self.tableWidget_6.horizontalHeader()
        header_3.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_3.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        header_4 = self.tableWidget_8.horizontalHeader()
        header_4.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header_4.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

    def Back(self):
        while self.tableWidget_3.rowCount() > 0:
            self.tableWidget_3.removeRow(0)
        self.lineEdit.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        self.lineEdit_2.clear()

        while self.tableWidget_9.rowCount() > 0:
            self.tableWidget_9.removeRow(0)
        self.lineEdit_3.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_2.setScene(scene)
        self.lineEdit_4.clear()

        while self.tableWidget_5.rowCount() > 0:
            self.tableWidget_5.removeRow(0)
        self.lineEdit_5.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_3.setScene(scene)
        self.lineEdit_6.clear()

        while self.tableWidget_6.rowCount() > 0:
            self.tableWidget_6.removeRow(0)
        self.lineEdit_7.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_4.setScene(scene)
        self.lineEdit_8.clear()

        while self.tableWidget_7.rowCount() > 0:
            self.tableWidget_7.removeRow(0)
        self.lineEdit_9.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_5.setScene(scene)
        self.lineEdit_10.clear()

        while self.tableWidget_8.rowCount() > 0:
            self.tableWidget_8.removeRow(0)
        self.lineEdit_11.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_6.setScene(scene)
        self.lineEdit_12.clear()

        while self.tableWidget_15.rowCount() > 0:
            self.tableWidget_15.removeRow(0)
        self.lineEdit_27.clear()
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView_13.setScene(scene)
        self.lineEdit_28.clear()

        self.tabWidget.setCurrentIndex(0)

    def FCFS_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def RR_Choices_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def RR_Tab(self):
        self.tabWidget.setCurrentIndex(3)
    
    def Priority_RR_Tab(self):
        self.tabWidget.setCurrentIndex(4)

    def SJF_Choices_Tab(self):
        self.tabWidget.setCurrentIndex(5)

    def Priority_Choices_Tab(self):
        self.tabWidget.setCurrentIndex(8)

    def SJF_Tab(self):
        self.tabWidget.setCurrentIndex(6)

    def SRTF_Tab(self):
        self.tabWidget.setCurrentIndex(7)

    def Priority_Tab(self):
        self.tabWidget.setCurrentIndex(9)

    def Preemptive_Priority_Tab(self):
        self.tabWidget.setCurrentIndex(10)

    def Table_FCFS(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(scene)
            self.lineEdit_2.clear()
            number_str = self.lineEdit.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_3.setRowCount(i)
                        self.tableWidget_3.insertRow(i)
                        self.tableWidget_3.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Re-enter the number of processes")
            else:
                QMessageBox.information(self, "Warning", "Re-enter the number of processes")
        except:
            QMessageBox.information(self, "Warning", "Re-enter the number of processes")

    def FCFS(self):
        try:
            n = int(self.lineEdit.text())
            tasks = []
            for i in range(n):
                if self.tableWidget_3.item(i, 0).text() not in tasks:
                    p_name = self.tableWidget_3.item(i, 0).text()
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the process name")
                    return

                if float(self.tableWidget_3.item(i, 1).text()) >= 0.0:
                    arrival = float(self.tableWidget_3.item(i, 1).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the process arrival time")
                    return
                if float(self.tableWidget_3.item(i, 2).text()) >= 0.0:
                    bur = float(self.tableWidget_3.item(i, 2).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the process burst time")
                    return
                tasks.append(Task(p_name, arrival, bur))

            # arrival_time ???????????? sorting.
            tasks = sorted(tasks, key = lambda x: (x.arrival_time))
            gant = Gant_chart()
            current_time = 0

            for task in tasks:
                # ??? task ?????? waiting_time, response_time, turnaround_time ??????
                if current_time < task.arrival_time:
                    none_time = task.arrival_time - current_time
                    gant.add(None, none_time)
                    current_time = task.arrival_time

                task.waiting_time = current_time-task.arrival_time
                task.response_time = current_time-task.arrival_time
                current_time += task.burst_time
                task.turnaround_time = current_time-task.arrival_time

                # gant chart ??????
                gant.add(task.pid, task.burst_time)

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(scene)
            scale = Main.scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            times = list(itertools.accumulate(gant.used_times))
            pids = gant.pids
            for i in range(len(times)):
                if i == 0:
                    timetext = QGraphicsSimpleTextItem('0.0')
                    scene.addItem(timetext)
                    timetext.setPos(0, 85)
                    timetext.setScale(1.5)
                    timetext = QGraphicsSimpleTextItem(str(float(times[0])))
                    scene.addItem(timetext)
                    timetext.setPos(times[0] * scale, 85)
                    timetext.setScale(1.5)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[0] * scale, 80))
                    scene.addRect(r, pen)
                    process_text = QGraphicsSimpleTextItem(str(pids[0]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[0] + 0) / 2, 30)
                    process_text.setScale(0.8)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[i] * scale, 80))
                    scene.addRect(r, pen)

                    process_text = QGraphicsSimpleTextItem(str(pids[i]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[i] + times[i - 1]) / 2, 30)
                    process_text.setScale(0.8)

                    timetext = QGraphicsSimpleTextItem(str(float(times[i])))
                    scene.addItem(timetext)
                    timetext.setPos(times[i] * scale, 85)
                    timetext.setScale(1.5)

            self.lineEdit_2.setText('  '+str("%.2f" % (get_ART(tasks))))
            self.lineEdit_31.setText('  '+str("%.2f" % (get_AWT(tasks))))
            self.lineEdit_30.setText('  '+str("%.2f" % (get_ATT(tasks))))


        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes wtf")


    def Table_SJF(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_3.setScene(scene)
            self.lineEdit_6.clear()
            number_str = self.lineEdit_5.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_5.setRowCount(i)
                        self.tableWidget_5.insertRow(i)
                        self.tableWidget_5.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")



    def SJF(self):
        try:
            n = int(self.lineEdit_5.text())
            tasks = []
            for i in range(n):
                if self.tableWidget_5.item(i, 0).text() not in tasks:
                    p_name = self.tableWidget_5.item(i, 0).text()
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return

                if float(self.tableWidget_5.item(i, 1).text()) >= 0:
                    arrival = float(self.tableWidget_5.item(i, 1).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_5.item(i, 2).text()) >= 0:
                    bur = float(self.tableWidget_5.item(i, 2).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                tasks.append(Task(p_name, arrival, bur))

            # arrival_time ???????????? sorting.
            tasks = sorted(tasks, key = lambda x: (x.arrival_time, x.burst_time))
            gant = Gant_chart()
            current_time = 0

            # ready_queue ??????
            ready_queue = Ready_queue()
            task_scores = []
            while ready_queue or tasks:
                if not ready_queue:
                    current_task = tasks.pop(0)
                    none_time = current_task.arrival_time - current_time
                    gant.add(None, none_time)
                    current_time = current_task.arrival_time
                else:
                    current_task = ready_queue.pop(0)

                current_task.waiting_time = current_time-current_task.arrival_time
                current_task.response_time = current_time-current_task.arrival_time
                current_time += current_task.burst_time
                current_task.turnaround_time = current_time-current_task.arrival_time
                gant.add(current_task.pid, current_task.burst_time)
                task_scores.append(current_task)

                while tasks:
                    if tasks[0].arrival_time <= current_time:
                        task = tasks.pop(0)
                        ready_queue.insert_process(task, key=lambda x: (x.burst_time))
                    else:
                        break

            times, pids = list(itertools.accumulate(gant.used_times)), gant.pids
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_3.setScene(scene)
            scale = Main.scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            for i in range(len(times)):
                if i == 0:
                    timtext = QGraphicsSimpleTextItem('0.0')
                    scene.addItem(timtext)
                    timtext.setPos(0, 85)
                    timtext.setScale(1.5)
                    timtext = QGraphicsSimpleTextItem(str(times[0]))
                    scene.addItem(timtext)
                    timtext.setPos(times[0] * scale, 85)
                    timtext.setScale(1.5)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[0] * scale, 80))
                    scene.addRect(r, pen)
                    process_text = QGraphicsSimpleTextItem(str(pids[0]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[0] + 0) / 2, 30)
                    process_text.setScale(0.8)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[i] * scale, 80))
                    scene.addRect(r, pen)

                    process_text = QGraphicsSimpleTextItem(str(pids[i]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[i] + times[i - 1]) / 2, 30)
                    process_text.setScale(0.8)

                    timetext = QGraphicsSimpleTextItem(str(float(times[i])))
                    scene.addItem(timetext)
                    timetext.setPos(times[i] * scale, 85)
                    timetext.setScale(1.5)

            self.lineEdit_6.setText('  '+str("%.2f" % (get_ART(task_scores))))
            self.lineEdit_35.setText('  '+str("%.2f" % (get_AWT(task_scores))))
            self.lineEdit_34.setText('  '+str("%.2f" % (get_ATT(task_scores))))
            
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")

    def Table_SRTF(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_4.setScene(scene)
            self.lineEdit_8.clear()
            number_str = self.lineEdit_7.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_6.setRowCount(i)
                        self.tableWidget_6.insertRow(i)
                        self.tableWidget_6.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")


    def SRTF(self):
        try:
            n = int(self.lineEdit_7.text())
            tasks = []
            for i in range(n):
                if self.tableWidget_6.item(i, 0).text() not in tasks:
                    p_name = self.tableWidget_6.item(i, 0).text()
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return

                if float(self.tableWidget_6.item(i, 1).text()) >= 0:
                    arrival = float(self.tableWidget_6.item(i, 1).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_6.item(i, 2).text()) >= 0:
                    bur = float(self.tableWidget_6.item(i, 2).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                tasks.append(Task(p_name, arrival, bur))

            # arrival_time ???????????? sorting.
            tasks = sorted(tasks, key = lambda x: (x.arrival_time))
            gant = Gant_chart()
            current_time = 0

            # ready_queue ??????
            ready_queue = Ready_queue()
            task_scores = []
            while ready_queue or tasks:
                if not ready_queue:
                    current_task = tasks.pop(0)
                    none_time = current_task.arrival_time - current_time
                    gant.add(None, none_time)
                    current_time = current_task.arrival_time
                else:
                    current_task = ready_queue.pop(0)
                
                if tasks and (tasks[0].arrival_time < current_time+current_task.burst_time):
                    task = tasks.pop(0)
                    used_time = task.arrival_time-current_time
                    current_task.burst_time -= used_time
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_task.waiting_time -= used_time
                    current_time = task.arrival_time
                    gant.add(current_task.pid, used_time)

                    ready_queue.insert_process(current_task, key=lambda x: (x.burst_time))
                    ready_queue.insert_process(task, key=lambda x: (x.burst_time))
                else:
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_task.waiting_time += current_time-current_task.arrival_time
                    current_time += current_task.burst_time
                    current_task.turnaround_time = current_time-current_task.arrival_time
                    gant.add(current_task.pid, current_task.burst_time)
                    task_scores.append(current_task)

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_4.setScene(scene)
            scale = Main.scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            times = list(itertools.accumulate(gant.used_times))
            pids = gant.pids

            for i in range(len(times)):
                if i == 0:
                    timetext = QGraphicsSimpleTextItem('0.0')
                    scene.addItem(timetext)
                    timetext.setPos(0, 85)
                    timetext.setScale(1.5)
                    timetext = QGraphicsSimpleTextItem(str(float(times[0])))
                    scene.addItem(timetext)
                    timetext.setPos(times[0] * scale, 85)
                    timetext.setScale(1.5)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[0] * scale, 80))
                    scene.addRect(r, pen)
                    process_text = QGraphicsSimpleTextItem(str(pids[0]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[0] + 0) / 2, 30)
                    process_text.setScale(0.8)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[i] * scale, 80))
                    scene.addRect(r, pen)

                    process_text = QGraphicsSimpleTextItem(str(pids[i]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[i] + times[i - 1]) / 2, 30)
                    process_text.setScale(0.8)

                    timetext = QGraphicsSimpleTextItem(str(float(times[i])))
                    scene.addItem(timetext)
                    timetext.setPos(times[i] * scale, 85)
                    timetext.setScale(1.5)

            self.lineEdit_8.setText('  '+str("%.2f" % (get_ART(task_scores))))
            self.lineEdit_37.setText('  '+str("%.2f" % (get_AWT(task_scores))))
            self.lineEdit_36.setText('  '+str("%.2f" % (get_ATT(task_scores))))

        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")



    def Table_Priority(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_5.setScene(scene)
            self.lineEdit_10.clear()
            number_str = self.lineEdit_9.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_7.setRowCount(i)
                        self.tableWidget_7.insertRow(i)
                        self.tableWidget_7.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")

    def Priority(self):
        try:
            n = int(self.lineEdit_9.text())
            tasks = []
            for i in range(n):
                if self.tableWidget_7.item(i, 0).text() not in tasks:
                    p_name = self.tableWidget_7.item(i, 0).text()
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return

                if float(self.tableWidget_7.item(i, 1).text()) >= 0:
                    arrival = float(self.tableWidget_7.item(i, 1).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_7.item(i, 2).text()) >= 0:
                    bur = float(self.tableWidget_7.item(i, 2).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_7.item(i, 3).text()) >= 0:
                    priority = float(self.tableWidget_7.item(i, 3).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                tasks.append(Task(p_name, arrival, bur, priority))

            # arrival_time ???????????? sorting.
            tasks = sorted(tasks, key = lambda x: (x.arrival_time, x.priority))
            gant = Gant_chart()
            current_time = 0

            # ready_queue ??????
            ready_queue = Ready_queue()
            task_scores = []
            while ready_queue or tasks:
                if not ready_queue:
                    current_task = tasks.pop(0)
                    none_time = current_task.arrival_time - current_time
                    gant.add(None, none_time)
                    current_time = current_task.arrival_time
                else:
                    current_task = ready_queue.pop(0)

                current_task.waiting_time = current_time-current_task.arrival_time
                current_task.response_time = current_time-current_task.arrival_time
                current_time += current_task.burst_time
                current_task.turnaround_time = current_time-current_task.arrival_time
                gant.add(current_task.pid, current_task.burst_time)
                task_scores.append(current_task)

                while tasks:
                    if tasks[0].arrival_time <= current_time:
                        task = tasks.pop(0)
                        ready_queue.insert_process(task, key=lambda x: (x.priority))
                    else:
                        break
            

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_5.setScene(scene)
            scale = Main.scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            times = list(itertools.accumulate(gant.used_times))
            pids = gant.pids
            for i in range(len(times)):
                if i == 0:
                    timetext = QGraphicsSimpleTextItem('0.0')
                    scene.addItem(timetext)
                    timetext.setPos(0, 85)
                    timetext.setScale(1.5)
                    timetext = QGraphicsSimpleTextItem(str(float(times[0])))
                    scene.addItem(timetext)
                    timetext.setPos(times[0] * scale, 85)
                    timetext.setScale(1.5)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[0] * scale, 80))
                    scene.addRect(r, pen)
                    process_text = QGraphicsSimpleTextItem(str(pids[0]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[0] + 0) / 2, 30)
                    process_text.setScale(0.8)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[i] * scale, 80))
                    scene.addRect(r, pen)

                    process_text = QGraphicsSimpleTextItem(str(pids[i]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[i] + times[i - 1]) / 2, 30)
                    process_text.setScale(0.8)

                    timetext = QGraphicsSimpleTextItem(str(float(times[i])))
                    scene.addItem(timetext)
                    timetext.setPos(times[i] * scale, 85)
                    timetext.setScale(1.5)

            self.lineEdit_10.setText('  '+str("%.2f" % (get_ART(task_scores))))
            self.lineEdit_39.setText('  '+str("%.2f" % (get_AWT(task_scores))))
            self.lineEdit_38.setText('  '+str("%.2f" % (get_ATT(task_scores))))
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")

    def Table_RR(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_2.setScene(scene)
            self.lineEdit_4.clear()
            number_str = self.lineEdit_3.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_9.setRowCount(i)
                        self.tableWidget_9.insertRow(i)
                        self.tableWidget_9.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")

    def Table_Priority_RR(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_13.setScene(scene)
            self.lineEdit_28.clear()
            number_str = self.lineEdit_27.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_15.setRowCount(i)
                        self.tableWidget_15.insertRow(i)
                        self.tableWidget_15.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")


    def RR(self):
        try:
            n = int(self.lineEdit_3.text())
            tasks = []
            for i in range(n):
                if self.tableWidget_9.item(i, 0).text() not in tasks:
                    p_name = self.tableWidget_9.item(i, 0).text()
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return

                if float(self.tableWidget_9.item(i, 1).text()) >= 0:
                    arrival = float(self.tableWidget_9.item(i, 1).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_9.item(i, 2).text()) >= 0:
                    bur = float(self.tableWidget_9.item(i, 2).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                tasks.append(Task(p_name, arrival, bur))


            if float(self.lineEdit_13.text()) > 0:
                t_q = float(self.lineEdit_13.text())
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
                return

            # arrival_time ???????????? sorting.
            tasks = sorted(tasks, key = lambda x: (x.arrival_time))
            gant = Gant_chart()
            current_time = 0

            # ready_queue ??????
            ready_queue = Ready_queue()
            task_scores = []
            while ready_queue or tasks:
                if not ready_queue:
                    current_task = tasks.pop(0)
                    none_time = current_task.arrival_time - current_time
                    gant.add(None, none_time)
                    current_time = current_task.arrival_time
                else:
                    current_task = ready_queue.pop(0)

                if current_task.burst_time <= t_q:
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_task.waiting_time += current_time-current_task.arrival_time
                    current_time += current_task.burst_time
                    current_task.turnaround_time = current_time-current_task.arrival_time
                    gant.add(current_task.pid, current_task.burst_time)
                    current_task.burst_time = 0
                    task_scores.append(current_task)
                else:
                    current_task.burst_time -= t_q
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_task.waiting_time -= t_q
                    current_time += t_q
                    gant.add(current_task.pid, t_q)

                while tasks:
                    # ????????? ?????? ?????? ????????? process ?????? ready queue???
                    if tasks[0].arrival_time <= current_time:
                        task = tasks.pop(0)
                        ready_queue.insert_process(task, key=None)
                    else:
                        break
                if current_task.burst_time != 0:
                    ready_queue.insert_process(current_task, key=None)
            

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_2.setScene(scene)
            scale = Main.scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            times, pids = list(itertools.accumulate(gant.used_times)), gant.pids
            for i in range(len(times)):
                if i == 0:
                    timetext = QGraphicsSimpleTextItem('0.0')
                    scene.addItem(timetext)
                    timetext.setPos(0, 85)
                    timetext.setScale(1.5)
                    timetext = QGraphicsSimpleTextItem(str(float(times[0])))
                    scene.addItem(timetext)
                    timetext.setPos(times[0] * scale, 85)
                    timetext.setScale(1.5)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[0] * scale, 80))
                    scene.addRect(r, pen)
                    process_text = QGraphicsSimpleTextItem(str(pids[0]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[0] + 0) / 2, 30)
                    process_text.setScale(0.8)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[i] * scale, 80))
                    scene.addRect(r, pen)

                    process_text = QGraphicsSimpleTextItem(str(pids[i]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[i] + times[i - 1]) / 2, 30)
                    process_text.setScale(0.8)

                    timetext = QGraphicsSimpleTextItem(str(float(times[i])))
                    scene.addItem(timetext)
                    timetext.setPos(times[i] * scale, 85)
                    timetext.setScale(1.5)

            self.lineEdit_4.setText('  '+str("%.2f" % (get_ART(task_scores))))
            self.lineEdit_33.setText('  '+str("%.2f" % (get_AWT(task_scores))))
            self.lineEdit_32.setText('  '+str("%.2f" % (get_ATT(task_scores))))


        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")

    def Priority_RR(self):
        try:
            n = int(self.lineEdit_27.text())
            tasks = []
            for i in range(n):
                if self.tableWidget_15.item(i, 0).text() not in tasks:
                    p_name = self.tableWidget_15.item(i, 0).text()
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return

                if float(self.tableWidget_15.item(i, 1).text()) >= 0:
                    arrival = float(self.tableWidget_15.item(i, 1).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_15.item(i, 2).text()) >= 0:
                    bur = float(self.tableWidget_15.item(i, 2).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return

                if int(self.tableWidget_15.item(i, 3).text()) >= 0:
                    priority = int(self.tableWidget_15.item(i, 3).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                tasks.append(Task(p_name, arrival, bur, priority))


            if float(self.lineEdit_29.text()) > 0:
                t_q = float(self.lineEdit_29.text())
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
                return

            # arrival_time ???????????? sorting.
            tasks = sorted(tasks, key = lambda x: (x.arrival_time, x.priority))
            gant = Gant_chart()
            current_time = 0

            # ready_queue ??????
            ready_queue = Ready_queue()
            task_scores = []
            while ready_queue or tasks:
                if not ready_queue:
                    current_task = tasks.pop(0)
                    none_time = current_task.arrival_time - current_time
                    gant.add(None, none_time)
                    current_time = current_task.arrival_time
                else:
                    current_task = ready_queue.pop(0)
                
                if current_task.burst_time <= t_q:            
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_task.waiting_time += current_time-current_task.arrival_time
                    current_time += current_task.burst_time
                    current_task.turnaround_time = current_time-current_task.arrival_time
                    gant.add(current_task.pid, current_task.burst_time)
                    current_task.burst_time = 0
                    task_scores.append(current_task)
                else:
                    current_task.burst_time -= t_q
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_task.waiting_time -= t_q
                    current_time += t_q
                    gant.add(current_task.pid, t_q)

                while tasks:
                    # ????????? ?????? ?????? ????????? process ?????? ready queue???
                    if tasks[0].arrival_time <= current_time:
                        task = tasks.pop(0)
                        ready_queue.insert_process(task, key=lambda x: (x.priority))
                    else:
                        break

                if current_task.burst_time != 0:
                    ready_queue.insert_process(current_task, key=lambda x: (x.priority))
            

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_13.setScene(scene)
            scale = Main.scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            times, pids = list(itertools.accumulate(gant.used_times)), gant.pids
            for i in range(len(times)):
                if i == 0:
                    timetext = QGraphicsSimpleTextItem('0.0')
                    scene.addItem(timetext)
                    timetext.setPos(0, 85)
                    timetext.setScale(1.5)
                    timetext = QGraphicsSimpleTextItem(str(float(times[0])))
                    scene.addItem(timetext)
                    timetext.setPos(times[0] * scale, 85)
                    timetext.setScale(1.5)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[0] * scale, 80))
                    scene.addRect(r, pen)
                    process_text = QGraphicsSimpleTextItem(str(pids[0]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[0] + 0) / 2, 30)
                    process_text.setScale(0.8)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[i] * scale, 80))
                    scene.addRect(r, pen)

                    process_text = QGraphicsSimpleTextItem(str(pids[i]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[i] + times[i - 1]) / 2, 30)
                    process_text.setScale(0.8)

                    timetext = QGraphicsSimpleTextItem(str(float(times[i])))
                    scene.addItem(timetext)
                    timetext.setPos(times[i] * scale, 85)
                    timetext.setScale(1.5)

            self.lineEdit_28.setText('  '+str("%.2f" % (get_ART(task_scores))))
            self.lineEdit_41.setText('  '+str("%.2f" % (get_AWT(task_scores))))
            self.lineEdit_40.setText('  '+str("%.2f" % (get_ATT(task_scores))))


        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")


    def Table_Preemptive_Priority(self):
        try:
            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_6.setScene(scene)
            self.lineEdit_12.clear()
            number_str = self.lineEdit_11.text()
            if number_str != '' and int(number_str) > 0:
                try:
                    n = int(number_str)
                    for i in range(n):
                        self.tableWidget_8.setRowCount(i)
                        self.tableWidget_8.insertRow(i)
                        self.tableWidget_8.setItem(0, i, QTableWidgetItem(str('')))
                except:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
            else:
                QMessageBox.information(self, "Warning", "Re-enter the processes")
        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")


    def Preemptive_Priority(self):
        try:
            n = int(self.lineEdit_11.text())
            tasks = []
            for i in range(n):
                if self.tableWidget_8.item(i, 0).text() not in tasks:
                    p_name = self.tableWidget_8.item(i, 0).text()
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return

                if float(self.tableWidget_8.item(i, 1).text()) >= 0:
                    arrival = float(self.tableWidget_8.item(i, 1).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_8.item(i, 2).text()) >= 0:
                    bur = float(self.tableWidget_8.item(i, 2).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                if float(self.tableWidget_8.item(i, 3).text()) >= 0:
                    priority = float(self.tableWidget_8.item(i, 3).text())
                else:
                    QMessageBox.information(self, "Warning", "Re-enter the processes")
                    return
                tasks.append(Task(p_name, arrival, bur, priority))

            # arrival_time ???????????? sorting.
            tasks = sorted(tasks, key = lambda x: (x.arrival_time))
            gant = Gant_chart()
            current_time = 0

            # ready_queue ??????
            ready_queue = Ready_queue()
            task_scores = []
            while ready_queue or tasks:
                if not ready_queue:
                    current_task = tasks.pop(0)
                    none_time = current_task.arrival_time - current_time
                    gant.add(None, none_time)
                    current_time = current_task.arrival_time
                else:
                    current_task = ready_queue.pop(0)
                
                if tasks and (tasks[0].arrival_time < current_time+current_task.burst_time):
                    task = tasks.pop(0)
                    used_time = task.arrival_time-current_time
                    current_task.burst_time -= used_time
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_task.waiting_time -= used_time
                    current_time = task.arrival_time
                    gant.add(current_task.pid, used_time)

                    ready_queue.insert_process(current_task, key=lambda x: (x.priority))
                    ready_queue.insert_process(task, key=lambda x: (x.priority))
                else:
                    current_task.waiting_time += current_time-current_task.arrival_time
                    if current_task.response_time is None:
                        current_task.response_time = current_time-current_task.arrival_time
                    current_time += current_task.burst_time
                    current_task.turnaround_time = current_time-current_task.arrival_time
                    gant.add(current_task.pid, current_task.burst_time)
                    task_scores.append(current_task)

            scene = QtWidgets.QGraphicsScene()
            self.graphicsView_6.setScene(scene)
            scale = Main.scale
            pen = QtGui.QPen(QtCore.Qt.black, 3)
            times, pids = list(itertools.accumulate(gant.used_times)), gant.pids
            for i in range(len(times)):
                if i == 0:
                    timetext = QGraphicsSimpleTextItem('0.0')
                    scene.addItem(timetext)
                    timetext.setPos(0, 85)
                    timetext.setScale(1.5)
                    timetext = QGraphicsSimpleTextItem(str(float(times[0])))
                    scene.addItem(timetext)
                    timetext.setPos(times[0] * scale, 85)
                    timetext.setScale(1.5)
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[0] * scale, 80))
                    scene.addRect(r, pen)
                    process_text = QGraphicsSimpleTextItem(str(pids[0]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[0] + 0) / 2, 30)
                    process_text.setScale(0.8)

                else:
                    r = QtCore.QRectF(QtCore.QPointF(10, 0), QtCore.QSizeF(times[i] * scale, 80))
                    scene.addRect(r, pen)

                    process_text = QGraphicsSimpleTextItem(str(times[i]))
                    scene.addItem(process_text)
                    process_text.setPos(scale * (times[i] + times[i - 1]) / 2, 30)
                    process_text.setScale(0.8)

                    timetext = QGraphicsSimpleTextItem(str(float(times[i])))
                    scene.addItem(timetext)
                    timetext.setPos(times[i] * scale, 85)
                    timetext.setScale(1.5)

            self.lineEdit_12.setText('  '+str("%.2f" % (get_ART(task_scores))))
            self.lineEdit_43.setText('  '+str("%.2f" % (get_AWT(task_scores))))
            self.lineEdit_42.setText('  '+str("%.2f" % (get_ATT(task_scores))))

        except:
            QMessageBox.information(self, "Warning", "Re-enter the processes")


def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
