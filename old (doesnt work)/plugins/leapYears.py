def LeapYears(calc1):
    def backButton(self):
        self.backButton = QLabel(self)
        self.backButton.setGeometry(50, 50, 100, 30)
        self.backButton.setText()
    
    try:
        year = calc1
    except Exception:
        print("oops, that was not a valid number! Please try again.")
            
    mod4year = int(year) % 4
    mod100year = int(year) % 100
    mod400year = int(year) % 400
                    
    if mod4year == 0 and mod100year == 0 and mod400year == 0:
        print("true")
    elif mod4year == 0 and mod100year != 0:
        print("true")
    else:
        print("false")