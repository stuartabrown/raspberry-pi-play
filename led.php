<?php
if (!empty($_GET["action"])) {
  $output = shell_exec("sudo python /home/pi/raspberry-pi-play/webOnOffLED.py ".strtolower($_GET["action"])) ;
  echo "TURNING LED: ". strtoupper($_GET["action"]);
}
else {
    print "foo";
}
?>
<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="get">
On <input type="radio" name="action" value="on" onchange="javascript:submit()"/> 
Off <input type="radio" name="action" value="off" onchange="javascript:submit()"/> <br/>
</form>