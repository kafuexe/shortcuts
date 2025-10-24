#Requires AutoHotkey v2.0
#Include FunctionRunner.ahk

Functions := {
    PlayPause: () =>Send("{Media_Play_Pause}"),
    NextTrack:() => Send("{Media_Next}"),
    PreviousTrack:() => Send("{Media_Prev}"),
    Stop:() => Send("{Media_Stop}"),
}
 
Run(Functions, A_Args)
ExitApp