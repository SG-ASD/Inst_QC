'use strict';

/**
 * 저장 버튼 클릭 시 팝업창 띄우기
 */
function alert_save(){
    alert("저장되었습니다.")
}

function onchange_check_attachment() {
    const Attachment_CoverSafety_Report = document.getElementById('Attachment_CoverSafety_Report');
    const Attachment_Barcode_Report = document.getElementById('Attachment_Barcode_Report');
    const Attachment_Position_Report = document.getElementById('Attachment_Position_Report');
    const Attachment_Declaration = document.getElementById('Attachment_Declaration');
    const Attachment_Declaration_HHS = document.getElementById('Attachment_Declaration_HHS');
    const Attachment_Measurement_Protocol = document.getElementById('Attachment_Measurement_Protocol');
    const Attachment_ElectricalSafety_Report = document.getElementById('Attachment_ElectricalSafety_Report');

    Attachment_CoverSafety_Report.click()
    Attachment_Barcode_Report.click()
    Attachment_Position_Report.click()
    Attachment_Declaration.click()
    Attachment_Declaration_HHS.click()
    Attachment_Measurement_Protocol.click()
    Attachment_ElectricalSafety_Report.click()
}