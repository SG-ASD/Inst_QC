'use strict';

/**
 * Tool 선택 시
 */
function Cal_Get_Info(obj) {
    const Calibration_Txt = document.getElementById('HardWare_CalibrationTool')
    Calibration_Txt.value = obj.value
}

function Barcode_Get_Info(obj) {
    const Barcode_Txt = document.getElementById('HardWare_BarcodeCarrier')
    Barcode_Txt.value = obj.value

}