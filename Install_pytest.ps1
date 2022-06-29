$user = $env:USERNAME
#$root = "C:\Users\$user\AppData\Local\Programs\Python\Python39"
$root = "C:\Python39"
$pip = Join-Path -Path $root -ChildPath "Scripts\pip.exe"
$Package = Join-Path -Path $root -ChildPath "Lib\site-packages"
$pytestPath = Join-Path -Path $Package -ChildPath "pytest"
$seleniumPath = Join-Path -Path $Package -ChildPath "selenium"
$Plugins = @("pytest","selenium")

function Generate-Html([array]$results)
{
    $rows="<p>MVT python component python for $vision</p>"
    $rows+="<p>Hi All, here is the configurations report for the running MVT machines.</p>"

     ForEach($_ in $results)
    {
        if($_.Outcome -ne "Passed")
        {
             $row="<tr class=`"error`"><td>"+$_.Id+"</td><td>"+$_.Outcome+"</td></tr>"
        }
        else{$row="<tr><td>"+$_.Id+"</td><td>"+$_.Outcome+"</td></tr>"}
        $body+=$row
    }
    $style="<style>.error{background-color: `"red`"} table,tr,td,th{border: solid 1px; border-spacing: 1px;} table{width:800}</style>"
    $html="<!DOCTYPE html><html>"+$style+$rows+"<table id=`"table`"><tr><th>ID</th><th>Outcome</th></tr>"+$body+"</table> </html>"
    return $html
}
Function AnalysisResult($sResultPath,$Component)
{
    function newResultObj($ID,$Outcome)
    {
        $obj=New-Object PSObject
        $Obj|Add-Member -MemberType NoteProperty -Name "ID" -Value $ID
        $Obj|Add-Member -MemberType NoteProperty -Name "Outcome" -Value $Outcome
        return $Obj
    }
    if(Test-Path -Path $sResultPath)
    {
    $Outcome = "Passed"
    }else{
    $Outcome = "Failed"
    }
    $ID = $Component
    $obj = newResultObj -ID $ID -Outcome $Outcome
    return $obj
 }
Function TestComponent($packPath, $Component)
{
  
    $res=(AnalysisResult -sResultPath $packPath -Component $Component)
    Write-Log -Message "Test result: $res.Result"

    $global:results+=$res
    
}
Set-Location -Path $root
foreach($Plugin in $Plugins)
{
    $process = Start-Process -FilePath $pip -ArgumentList "install $Plugin" -PassThru
    while($process.Responding)
    {
        Start-Sleep -Seconds 1
    }
}
$global:results=[array]@()
TestComponent -packPath $pytestPath -Component "pytest"
TestComponent -packPath $seleniumPath -Component "selenium"
Write-Host $results
$html=Generate-Html -results $results
Send-MailMessage -From "MVT@aspentech.com" -To "ziru.huang@aspentech.com", "will.you@aspentech.com" -Subject "Python Component Report for $vision " -Body $html -SmtpServer smtp.aspentech.local -BodyAsHtml


