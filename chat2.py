ef read_file(filename):
    lines = []
    with open (filename, "r", encoding = 'utf-8-sig') as f:#讀取檔案
            for line in f:
                 lines.append(line.strip())
    return lines    
def convert(lines):
    Allen_Word_count = 0
    Allen_Sticker_count = 0
    Allen_Image_count = 0
    Viki_Word_count = 0
    Viki_Sticker_count = 0
    Viki_Image_count = 0
    s = []
    for line in lines:
        s = line.split(" ")
        time = s[0]
        person = s[1]
        if person == "Allen" :
            if s[2] == "貼圖":
                Allen_Sticker_count += 1
            elif s[2] == "圖片":
                Allen_Image_count += 1
            else:
                for message in s[2:]:
                    Allen_Word_count += len(message)
        elif person == "Viki" :
            if s[2] == "貼圖":
                Viki_Sticker_count += 1
            elif  s[2] == "圖片":
                Viki_Image_count += 1
            else:
                for message in s[2:]:
                    Viki_Word_count += len(message)
            
    print("Allen講了" , Allen_Word_count , "個字")
    print("Allen了" , Allen_Image_count , "張圖片")
    print("Allen了" , Allen_Sticker_count , "個貼圖")
    
    print("Viki講了" , Viki_Word_count , "個字")
    print("Viki了" , Viki_Image_count , "張圖片")
    print("Viki傳了" , Viki_Sticker_count , "個貼圖")

            
def main():
    lines = read_file("LINE-Viki.txt") 
    s = convert(lines)
    
main()
