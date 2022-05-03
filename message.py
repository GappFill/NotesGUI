from PyQt5.QtWidgets import  QMessageBox


def Error(setText, setInformativeText, setWindowTitle):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(setText)
    msg.setInformativeText(setInformativeText)
    msg.setWindowTitle(setWindowTitle)
    msg.exec_()

def Information(setInformativeText, setWindowTitle):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(setInformativeText)
    msg.setWindowTitle(setWindowTitle)
    msg.setStandardButtons(QMessageBox.Yes)

    returnValue = msg.exec()
    if returnValue == QMessageBox.Yes:
        return True

def Warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Вы точно хотите выполнить удаление?")
    msg.setWindowTitle("Подтверждение операции")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

    returnValue = msg.exec()
    if returnValue == QMessageBox.Yes:
        return True

