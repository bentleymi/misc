#its powershell yo
function udpSend([string]$string) {
    $ip="127.0.0.1" #use quotes, but enter any IPv4 address
    $port=514 
    $msg=$string

    #create UDP .Net object
    $Address = [system.net.IPAddress]::Parse($ip) 
    $udpClient = New-Object system.net.sockets.udpclient

    #connect the UDP object to localhost and send the $msg ASCII encoded
    try{
         $udpClient.Connect($address, $port);
         $sendBytes=[Text.Encoding]::ASCII.GetBytes($msg)
         $udpClient.Send($sendBytes, $sendBytes.Length)
         $udpClient.Close();
    }  
    catch { write-host $error }
}
