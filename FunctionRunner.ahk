#Requires AutoHotkey v2.0
Run(Functions, ArgList) {
    if (ArgList.Length == 0) {
        MsgBox("No argument provided.")
        ExitApp
    }

    ; Access the first command-line argument from the provided array (ArgList).
    FunctionName := ArgList[1]
    
    if !IsObject(Functions) {
        MsgBox("Functions is not an object.")
        ExitApp
    }

    if !Functions.HasOwnProp(FunctionName) {
        MsgBox("Invalid argument provided: " FunctionName)
        ExitApp
    }


    Functions.%FunctionName%.Call()
    ExitApp
}
