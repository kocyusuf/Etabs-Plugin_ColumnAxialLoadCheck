import comtypes.client

ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
SapModel = ETABSObject.SapModel
ret = SapModel.Results.Setup.DeselectAllCasesAndCombosForOutput()
ret1 = SapModel.Results.Setup.SetComboSelectedForOutput("1.4g+1.6q")
ObjectElm = 0
NumberResults = 0
Obj = []
ObjSta = []
Elm = []
ElmSta = []
LoadCase = []
StepType = []
StepNum = []
P = []
V2 = []
V3 = []
T = []
M2 = []
M3 = []
ret2 = SapModel.Results.FrameForce("1", ObjectElm, NumberResults, Obj, ObjSta, Elm, ElmSta, LoadCase, StepType, StepNum, P, V2, V3, T, M2, M3)
print(ret2)
