## luckygame


###how can we get flag?

	flag is md5(passeword)
so our goal is to get admin's password

### Hint 1: You may want to test it on Ubuntu 16.04

#### bug1

- The GET and POST parameter has been escaped,but $_REQUEST and other env variable has not been escaped

- my_point function(115 line)

	$q = sprintf("SELECT * FROM users WHERE username = '%s'",filter($_SESSION['user']));

*exist injection  but length(username) must less than 24*

#### bug2

- user_log function(98 line)

	$q = sprintf("INSERT INTO logs VALUES (id+1,'%s')",
        filter($_SESSION['id'].'|'.$s));
        
*exist error blind injection(condition different)*

###bypass

^^^^^^^^^^^^🤠

- length limition

	you can regiest a username what admin' into @1,@2,@3,@4# first
	
	
- bypass >0 && <0

demo:

	<?php
	  if(!empty($_REQUEST['bet']) && (int)$_REQUEST['bet'] > 0){
	      echo 'bypass >0</br>';
	      if($_REQUEST['bet'] > 0) die("What?! you're cheater!");
	
	      echo 'success and you final payload is '.$_REQUEST['bet'];
	  }else{
	    echo 'fail';
	  }
	
	?>
	
php magic characteristic
you can input 1e-1000 to bypass it
	


	
