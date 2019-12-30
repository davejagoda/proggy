'from this: https://discuss.howtogeek.com/t/see-system-product-key-fast/12931
'invoke like this to get output on console
'cscript See_Product_Key.vbs
Set WshShell = CreateObject("WScript.Shell")
ConvertedKey = ConvertToKey(WshShell.RegRead("HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\DigitalProductId"))
'MsgBox will make a pop up, StdOut will write to stdout
'If you get an error, trying swapping the commenting on the next two lines
'MsgBox ConvertedKey
WScript.StdOut.WriteLine ConvertedKey

Function ConvertToKey(Key)
        Const KeyOffset = 52
        i = 28
        Chars = "BCDFGHJKMPQRTVWXY2346789"
        Do
                Cur = 0
                x = 14
                Do
                        Cur = Cur * 256
                        Cur = Key(x + KeyOffset) + Cur
                        Key(x + KeyOffset) = (Cur \ 24) And 255
                        Cur = Cur Mod 24
                        x = x -1
                Loop While x >= 0
                i = i -1
                KeyOutput = Mid(Chars, Cur + 1, 1) & KeyOutput
                If (((29 - i) Mod 6) = 0) And (i <> -1) Then
                        i = i -1
                        KeyOutput = "-" & KeyOutput
                End If
        Loop While i >= 0
        ConvertToKey = KeyOutput
End Function
