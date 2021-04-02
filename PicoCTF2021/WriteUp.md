# PicoCTF2021

# Sau đây là những bài mình giải được : 
  1. Cookies
  2. Scavenger Hunt
  3. Who are you ? 
  4. Super Serial 
  
# Web exploitation
  ## Cookies 
   Ở bài này khi truy cập http://mecury.picoctf.net:54219 trang web sẽ hiện giao diện thế này:
   
   <img src="https://i.imgur.com/NmcUoOv.png" title="source: imgur.com" />
    
   F12 xem nào :))
    
   <img src="https://i.imgur.com/IpRRezq.png" title="source: imgur.com" />
    
   Ok vào phần Network mình thấy web có gửi 1 Cookie có name=-1 
   Mình thử gõ snickerdoodle vào thử =)) 
    
   <img src="https://i.imgur.com/sBvOAcN.png" title="source: imgur.com" />
    
   Giá trị của cookie name=0
   Vậy giá trị name sẽ tăng dần ( ͡° ͜ʖ ͡°) vậy khi name tăng 1 giá trị nào đó thì sao 
   Mình dùng Burp Suite thử và gửi request đó đến phần Instruder =)) ở phần payload mình chọn Payload type là number và From = 0, To = 10 và Step = 1 và Start Attack 
   Kết quả sẽ ra thế này
   
   <img href="https://imgur.com/sDFleel"><img src="https://i.imgur.com/sDFleel.png" title="source: imgur.com" />
   
   Ở payload = 18 chỉ có Length = 1265 nên mình vào xem thử 
   
   <img href="https://imgur.com/ThIvUPs"><img src="https://i.imgur.com/ThIvUPs.png" title="source: imgur.com" />
   
   Vậy flag của bài này là **picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}**
   
  ## Scavenger Hunt
   Bài này khi mình truy cập đến http://mecury.picoctf.net:5080 thì sẽ được giao diện thế này
	
   <img src="https://i.imgur.com/hRkHawm.png" title="source: imgur.com" />
	
   Source file của bài này 
	
   <img src="https://i.imgur.com/pEMN53a.png" title="source: imgur.com" />
	
   OK ở đây có 1 phần của flag : **picoCTF{t**
	
   Mình xem thử trong file mycss.css
	
   <img src="https://i.imgur.com/gh5uVRu.png" title="source: imgur.com" />
	
   Và ở đây có 1 phần tiếp theo của flag : **h4ts_4_l0**. Tiếp tục xem tiếp myjs.js 
	
   <img src="https://i.imgur.com/dKhBWx1.png" title="source: imgur.com" />
	
   Ở đây mình thấy hint liên quan đến Google, mình thử truy cập /robots.txt xem 
	
   <img href="https://imgur.com/FOxYKuI"><img src="https://i.imgur.com/FOxYKuI.png" title="source: imgur.com" />
	
   Và được 1 phần tiếp theo của flag : **t_0f_pl4c** 
	
   Hint tiếp theo liên quan đến apache server nên mình thử vào .htaccess xem thử =))
	
   <img src="https://i.imgur.com/rlMScSk.png" title="source: imgur.com" />
	
   Và được 1 phần nữa của flag : **3s_2_lO0k**
	
   Hint tiếp theo liên quan đến việc làm web trên Mac và lưu nhiều thông tin trên đó nên mình truy cập vào .DS_Store
	
   <img src="https://i.imgur.com/qGPhv7Q.png" title="source: imgur.com" />
	
   Và phần cuối của flag : **_35844447}**

   Vậy flag của bài này là : **picoCTF{t h4ts_4_l0 t_0f_pl4c3s_2_lO0k_35844447}**
  ## Who are you ? 
   Bài này khi truy cập http://mecury.picoctf.net:36622 sẽ ra được giao diện như thế này
   
   <img src="https://i.imgur.com/2e5ZndL.png" title="source: imgur.com" />
   
   OK ở đây bài này có đề cập đến việc chỉ có PicoBrowser mới được phép truy cập, mình chuyển request sang Burp Suite vào phần Repeater và thay đổi giá trị User-agent: PicoBrowser

   <img src="https://i.imgur.com/Hr6ok2X.png" title="source: imgur.com" />
   
   Hint tiếp theo là bài này không tin người truy cập từ trang web khác, nên mình suy nghĩ đến việc thêm  header Referer(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) của chính bài này (Referer: http://mercury.picoctf.net:36622) và kết quả là
   
   <img src="https://i.imgur.com/8qcOVHN.png" title="source: imgur.com" />
   
   Hint tiếp theo liên quan đến thời gian vậy mình thêm header Date(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date) liên quan đến năm 2018 là được, mình thêm header Date: 1/1/2018
   
   <img src="https://i.imgur.com/fdCLuKP.png" title="source: imgur.com" />
   
   Hint tiếp theo liên quan đến header DNT (https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT) khi DNT: 0 người dùng sẽ cho phép việc theo dõi trên chính trang web này và ngược lại khi DNT: 1. Vậy ở đây mình thêm DNT = 0
   
   <img src="https://i.imgur.com/8mPwKgB.png" title="source: imgur.com" />
   
   Hint kế tiếp nói rằng chỉ tin những người truy cập đến từ Thụy Điển, ở đây mình nghĩ đến header X-Forwarded-For (https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) để đổi vị trí =))
   
   Mình kiếm 1 trang web ở Thụy Điển  https://sweden.se (Mình cũng không biết web này làm gì nhưng mà cảm ơn :3 ) 
   
   Và đổi địa chỉ web ra IP ( Mình dùng tool ở https://www.site24x7.com/find-ip-address-of-web-site.html và có được IP: 139.162.171.198 thêm header X-Forwarded-For: 139.162.171.198 vào thôi  
   
   <img src="https://i.imgur.com/Ys1bs4k.png" title="source: imgur.com" />
   
   Và hint kế tiếp nói rằng mình ở Thụy Điển nhưng không nói tiếng Thụy Điển ?? :D ?? . Mình thêm giá trị sv vào header Accept-Language là xong
   
   <img src="https://i.imgur.com/xPw6vzD.png" title="source: imgur.com" />
   
   Flag của bài này : picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_0da16bb2}
   
   