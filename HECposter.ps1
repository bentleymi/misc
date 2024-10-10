#powershell

Add-Type @"
using System.Net;
using System.Security.Cryptography.X509Certificates;
public class TrustAllCertsPolicy : ICertificatePolicy {
    public bool CheckValidationResult(
    ServicePoint srvPoint, X509Certificate certificate,
    WebRequest request, int certificateProblem) {
        return true;
    }
}
"@

[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy

# Set Tls versions
$allProtocols = [System.Net.SecurityProtocolType]'Ssl3,Tls,Tls11,Tls12'
[System.Net.ServicePointManager]::SecurityProtocol = $allProtocols

$token = "1c2b5388-0100-4458-8777-29acef7d1d71"
$server = "localhost"
$port = 8088
$url = "https://${server}:$port/services/collector/event"
$header = @{Authorization = "Splunk $token"}
$event = @{event = "hello world"} | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri $url -Headers $header -Body $event
