# CNSC CTF

# Web Exploitation 

  ## Web01
   Link: http://45.122.249.68:8080/
   
   Mình vào phần source code và dựa theo đó tạo một user và lấy được money = 2000 và tạo một cookie có giá trị username và money
   
   <img src="https://imgur.com/idgQiXI.png" title="source: imgur.com" />
   
   Để lấy được flag mình cần có money > 100000000
   
   <img src="https://imgur.com/zoV2y6B.png" title="source: imgur.com" />
   
   Ở đây mình cần thay đổi cookie theo yêu cầu của bài là được :)) 
   
   Mình dựa vào phần source code của đề bài và thấy web viết bằng Flask do đó mình thử payload {{7*7}} và thấy rằng có thể dựa theo SSTI (https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/)
   
   <img src="https://imgur.com/SBaeOyT.png" title="source: imgur.com" />

   Payload mình thử http://45.122.249.68:8080/{{config}}

   Và lấy được Secret key để tạo cookie 
   
   <img src="https://imgur.com/SBaeOyT.png" title="source: imgur.com" />

   Secret key **1235_anh_co_danh_roi_nhip_nao_khong**
   
   Mình vào source code của bài tạo sercet key như trên và sửa money = 100000001
   
   <img src="https://imgur.com/LhBbXtu.png" title="source: imgur.com" />

   Và có được flag của source code 
   
   <img src="https://imgur.com/X5X3gs5.png" title="source: imgur.com" />
   
   Và mình lấy cookie mới tạo vào web chính để lấy được flag **eyJtb25leSI6MTAwMDAwMDAxLCJ1c2VybmFtZSI6ImgzZGVzIn0.YH-wEw.s4-4Gjc5kvJXSOxalkKfak-1Wm8**
   
   <img src="https://imgur.com/rVMPz3D.png" title="source: imgur.com" />
   
   Vậy flag của bài : **flag{1s_th4t_55t1?}**