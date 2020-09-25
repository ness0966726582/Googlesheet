def Sendsheet():
    ###################################
    #            程式宣告區             #
    ###################################

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials 
    from pprint import pprint

    ###################################
    #           獲取授權與連結           #
    ###################################
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) #權限金鑰
    client = gspread.authorize(creds)
    sheet = client.open("test").sheet1

    ###################################
    #             寫入方式             #
    ###################################
    data=[1,2,3]
    x=1   #列暫存初始A(googlesheet)
    y=2   #行暫存初始2(googlesheet)
    z=0   #陣列的初始位置

    sheet.clear()
    while z < len(data):
        sheet.update_cell(y,x, data[z]) #功能2 更新CELL資料特定位置2行1列
        y = y + 1   #向下加入Sheet
        z = z + 1   #更新計數器
Sendsheet()