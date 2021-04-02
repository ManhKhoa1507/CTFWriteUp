# PicoCTF2021

#Sau đây là những bài mình giải được : 
  1. Cookies
  2. Scavenger Hunt
  3. Who are you ? 
  4. Super Serial 
  
#Web exploitation
  ##Cookies 
   Ở bài này khi truy cập http://mecury.picoctf.net:54219 trang web sẽ hiện giao diện thế này:
   <img href="https://imgur.com/NmcUoOv"><img src="https://i.imgur.com/NmcUoOv.png" title="source: imgur.com" />
    
   F12 xem nào :))
    
   <img href="https://imgur.com/IpRRezq"><img src="https://i.imgur.com/IpRRezq.png" title="source: imgur.com" />
    
   Ok vào phần Network mình thấy web có gửi 1 Cookie có name=-1 
   Mình thử gõ snickerdoodle vào thử =)) 
    
   <img href="https://imgur.com/sBvOAcN"><img src="https://i.imgur.com/sBvOAcN.png" title="source: imgur.com" />
    
   Giá trị của cookie name=0
   Vậy giá trị name sẽ tăng dần ( ͡° ͜ʖ ͡°) vậy khi name tăng 1 giá trị nào đó thì sao 
   Mình dùng Burp Suite thử và gửi request đó đến phần Instruder =)) ở phần payload mình chọn Payload type là number và From = 0, To = 10 và Step = 1 và Start Attack 
   Kết quả sẽ ra thế này
   
   <img href="https://imgur.com/sDFleel"><img src="https://i.imgur.com/sDFleel.png" title="source: imgur.com" />
   
   Ở payload = 18 chỉ có Length = 1265 nên mình vào xem thử 
   
   <img href="https://imgur.com/ThIvUPs"><img src="https://i.imgur.com/ThIvUPs.png" title="source: imgur.com" />
   
   Vậy flag của bài này là **picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}**