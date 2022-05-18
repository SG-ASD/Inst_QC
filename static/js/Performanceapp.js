'use strict';

/**
 * 저장 버튼 클릭 시 팝업창 띄우기
 */
function alert_save(){
    alert("저장되었습니다.")
}

/**
 * 검사성적서의 상위 select list에서 category 선택 시
 * 하위 select list에 해당 category의 subcategory 표시
 *
 * @param obj - 선택한 category
 */
function select_category(obj) {
    if (obj.value == "Appearance Inspection") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Packaging Condition">1) Packaging Condition</option>
            <option value="Appearance of instrument">2) Appearance of instrument</option>
            <option value="Instrument Accessories Kits">3) Instrument Accessories Kits</option>`;
    }
    else if (obj.value == "Electrical Test") {
        document.getElementById("inspection_subcategory").innerHTML = `
            {% load static %}
            <option value="">--항목 선택--</option>
            <option value="Electrical Test" href="{% url 'Electricalapp:update' target_Appearance.Instrument_SN_id %}">1) Electrical Test</option>
            <option value="{{ obj.value }}" href="{% url 'Electricalapp:update' target_Appearance.Instrument_SN_id %}">{{ obj.value }}</option>`;
    }
    else if (obj.value == "Hardware Adjustment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Hardware Adjustment">1) Hardware Adjustment</option>`;
    }
    else if (obj.value == "Performance Verification") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Performance Verification">1) Performance Verification</option>`;
    }
    else if (obj.value == "Attachment") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Attachment">1) Attachment</option>`;
    }
    else if (obj.value == "Accessories Kits") {
        document.getElementById("inspection_subcategory").innerHTML = `
            <option value="">--항목 선택--</option>
            <option value="Accessories Kits">1) Accessories Kits</option>`;
    }
}

/**
 * 검사성적서의 하위 select list에서 subcategory 선택 시
 * 해당 하위 subcategory 화면으로 이동
 *
 * @param obj - 선택한 subcategory
 */
function select_subcategory(obj) {
    alert(obj.value)
    alert(obj.href)
    if (obj.value == "Electrical Test"){
        document.location.href = "http://127.0.0.1:8000/QC/";
        // document.location.href = "{% url 'Electricalapp:update' target_Appearance.Instrument_SN_id %}"
    }
}

function onchange_check_Performance_first() {
    debugger
    const Perfomance_CoverSafety = document.getElementById('Perfomance_CoverSafety1');
    const Perfomance_Barcode = document.getElementById('Perfomance_Barcode1');
    const Perfomance_XYZpositioning = document.getElementById('Perfomance_XYZpositioning1');
    const Perfomance_HHS_temperature = document.getElementById('Perfomance_HHS_temperature1');
    const Perfomance_HHS_RPM = document.getElementById('Perfomance_HHS_RPM1');
    const Perfomance_Loading_TipCarrier = document.getElementById('Perfomance_Loading_TipCarrier1');
    const Perfomance_Loading_TubeCarrier = document.getElementById('Perfomance_Loading_TubeCarrier1');

    const Perfomance_Loading_mtpCarrier = document.getElementById('Perfomance_Loading_mtpCarrier1');
    const Perfomance_Loading_4mfxCarrier = document.getElementById('Perfomance_Loading_4mfxCarrier1');


    Perfomance_CoverSafety.click()
    Perfomance_Barcode.click()
    Perfomance_XYZpositioning.click()
    Perfomance_HHS_temperature.click()
    Perfomance_HHS_RPM.click()
    Perfomance_Loading_TipCarrier.click()
    Perfomance_Loading_TubeCarrier.click()
    Perfomance_Loading_mtpCarrier.click()
    Perfomance_Loading_4mfxCarrier.click()

}

function onchange_check_Performance_second() {
    const Perfomance_VFV_Accuracy300ul1 = document.getElementById('Perfomance_VFV_Accuracy300ul1_P');
    const Perfomance_VFV_Accuracy300ul2 = document.getElementById('Perfomance_VFV_Accuracy300ul2_P');
    const Perfomance_VFV_Accuracy300ul3 = document.getElementById('Perfomance_VFV_Accuracy300ul3_P');
    const Perfomance_VFV_Accuracy300ul4 = document.getElementById('Perfomance_VFV_Accuracy300ul4_P');
    const Perfomance_VFV_Accuracy300ul5 = document.getElementById('Perfomance_VFV_Accuracy300ul5_P');
    const Perfomance_VFV_Accuracy300ul6 = document.getElementById('Perfomance_VFV_Accuracy300ul6_P');
    const Perfomance_VFV_Accuracy300ul7 = document.getElementById('Perfomance_VFV_Accuracy300ul7_P');
    const Perfomance_VFV_Accuracy300ul8 = document.getElementById('Perfomance_VFV_Accuracy300ul8_P');

    const Perfomance_VFV_Precision300ul1 = document.getElementById('Perfomance_VFV_Precision300ul1_P');
    const Perfomance_VFV_Precision300ul2 = document.getElementById('Perfomance_VFV_Precision300ul2_P');
    const Perfomance_VFV_Precision300ul3 = document.getElementById('Perfomance_VFV_Precision300ul3_P');
    const Perfomance_VFV_Precision300ul4 = document.getElementById('Perfomance_VFV_Precision300ul4_P');
    const Perfomance_VFV_Precision300ul5 = document.getElementById('Perfomance_VFV_Precision300ul5_P');
    const Perfomance_VFV_Precision300ul6 = document.getElementById('Perfomance_VFV_Precision300ul6_P');
    const Perfomance_VFV_Precision300ul7 = document.getElementById('Perfomance_VFV_Precision300ul7_P');
    const Perfomance_VFV_Precision300ul8 = document.getElementById('Perfomance_VFV_Precision300ul8_P');

    const Perfomance_VFV_Accuracy1000ul1 = document.getElementById('Perfomance_VFV_Accuracy1000ul1_P');
    const Perfomance_VFV_Accuracy1000ul2 = document.getElementById('Perfomance_VFV_Accuracy1000ul2_P');
    const Perfomance_VFV_Accuracy1000ul3 = document.getElementById('Perfomance_VFV_Accuracy1000ul3_P');
    const Perfomance_VFV_Accuracy1000ul4 = document.getElementById('Perfomance_VFV_Accuracy1000ul4_P');
    const Perfomance_VFV_Accuracy1000ul5 = document.getElementById('Perfomance_VFV_Accuracy1000ul5_P');
    const Perfomance_VFV_Accuracy1000ul6 = document.getElementById('Perfomance_VFV_Accuracy1000ul6_P');
    const Perfomance_VFV_Accuracy1000ul7 = document.getElementById('Perfomance_VFV_Accuracy1000ul7_P');
    const Perfomance_VFV_Accuracy1000ul8 = document.getElementById('Perfomance_VFV_Accuracy1000ul8_P');

    const Perfomance_VFV_Precision1000ul1 = document.getElementById('Perfomance_VFV_Precision1000ul1_P');
    const Perfomance_VFV_Precision1000ul2 = document.getElementById('Perfomance_VFV_Precision1000ul2_P');
    const Perfomance_VFV_Precision1000ul3 = document.getElementById('Perfomance_VFV_Precision1000ul3_P');
    const Perfomance_VFV_Precision1000ul4 = document.getElementById('Perfomance_VFV_Precision1000ul4_P');
    const Perfomance_VFV_Precision1000ul5 = document.getElementById('Perfomance_VFV_Precision1000ul5_P');
    const Perfomance_VFV_Precision1000ul6 = document.getElementById('Perfomance_VFV_Precision1000ul6_P');
    const Perfomance_VFV_Precision1000ul7 = document.getElementById('Perfomance_VFV_Precision1000ul7_P');
    const Perfomance_VFV_Precision1000ul8 = document.getElementById('Perfomance_VFV_Precision1000ul8_P');



    Perfomance_VFV_Accuracy300ul1.click()
    Perfomance_VFV_Accuracy300ul2.click()
    Perfomance_VFV_Accuracy300ul3.click()
    Perfomance_VFV_Accuracy300ul4.click()
    Perfomance_VFV_Accuracy300ul5.click()
    Perfomance_VFV_Accuracy300ul6.click()
    Perfomance_VFV_Accuracy300ul7.click()
    Perfomance_VFV_Accuracy300ul8.click()


    Perfomance_VFV_Precision300ul1.click()
    Perfomance_VFV_Precision300ul2.click()
    Perfomance_VFV_Precision300ul3.click()
    Perfomance_VFV_Precision300ul4.click()
    Perfomance_VFV_Precision300ul5.click()
    Perfomance_VFV_Precision300ul6.click()
    Perfomance_VFV_Precision300ul7.click()
    Perfomance_VFV_Precision300ul8.click()

    Perfomance_VFV_Accuracy1000ul1.click()
    Perfomance_VFV_Accuracy1000ul2.click()
    Perfomance_VFV_Accuracy1000ul3.click()
    Perfomance_VFV_Accuracy1000ul4.click()
    Perfomance_VFV_Accuracy1000ul5.click()
    Perfomance_VFV_Accuracy1000ul6.click()
    Perfomance_VFV_Accuracy1000ul7.click()
    Perfomance_VFV_Accuracy1000ul8.click()

    Perfomance_VFV_Precision1000ul1.click()
    Perfomance_VFV_Precision1000ul2.click()
    Perfomance_VFV_Precision1000ul3.click()
    Perfomance_VFV_Precision1000ul4.click()
    Perfomance_VFV_Precision1000ul5.click()
    Perfomance_VFV_Precision1000ul6.click()
    Perfomance_VFV_Precision1000ul7.click()
    Perfomance_VFV_Precision1000ul8.click()

}