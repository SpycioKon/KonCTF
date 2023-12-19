<?php
if(isset($_GET['source'])){
    highlight_file(__FILE__);
}
class User{
    protected $name;
    protected $isRole;
    function __construct($name){
        $this->name = $name;
        $this->isRole = false;
    }
    function setName($name){
        $this->name = $name;
    }
    function getRole(){
        return $this->isRole;
    }
}
?>
