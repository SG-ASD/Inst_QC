'use strict';

/**
 * 저장 버튼 클릭 시 팝업창 띄우기
 */
function alert_save(){
    alert("저장되었습니다.")
}

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
function Cal_Get_Info(obj) {
    const Calibration_Txt = document.getElementById('HardWare_CalibrationTool')
    Calibration_Txt.value = obj.value
}

function openTextFile() {
    let input = document.querySelector('input');
    let textarea = document.querySelector('textarea')

    input.addEventListener('change', () => {
       let files = input.files;
       if(files.length == 0 ) return;

       const  file = files[0];

       let reader = new FileReader();

       reader.onload = (e) => {
           const file = e.target.result;
           const lines = file.split(/\r\n|\n/);
           textarea.value = lines.join('\n');
       };
       reader.onerror = (e) => alert(e.target.error.name);
       reader.readAsText(file);
    });
}
function Integer_Validate() {
    //X-Arm Adjust Arm Z using PIP left
    $(document).on("keyup", "input[name^=HardWare_XArm_left]", function() {
    var val= $(this).val();

    if(val < -5 || val > 5) {
        alert("-5~5 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //X-Arm Adjust Arm Z using PIP Right
    $(document).on("keyup", "input[name^=HardWare_XArm_right]", function() {
    var val= $(this).val();

    if(val < -5 || val > 5) {
        alert("-5~5 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //X-Arm Check Arm Diff
    $(document).on("keyup", "input[name^=HardWare_XArm_Diff]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
}

function Channel_AdjustX_Validate() {
     //P1 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev1]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
     //P1 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt1]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

     //P2 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev2]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P2 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt2]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P3 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev3]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P3 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt3]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P4 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev4]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P4 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt4]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P5 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev5]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P5 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt5]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P6 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev6]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P6 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt6]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P7 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev7]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P7 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt7]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P8 dev x
    $(document).on("keyup", "input[name^=HardWare_Xdev8]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P8 tilt x
    $(document).on("keyup", "input[name^=HardWare_Xtilt8]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
}

function Channel_AdjustY_Validate() {
    //P1 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt1]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

     //P2 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt2]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

     //P3 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt3]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

     //P4 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt4]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

     //P5 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt5]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

     //P6 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt6]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P7 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt7]", function() {
    var val= $(this).val();

    if(val < -10 || val > 10) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P8 tilt Y
    $(document).on("keyup", "input[name^=HardWare_Ytilt8]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
}

function Channel_PIPXY_Validate(){
    //P8 tilt Y
    $(document).on("keyup", "input[name^=HardWare_PIP_X1]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-10~10 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P1 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y1]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P2 PIP X1
    $(document).on("keyup", "input[name^=HardWare_PIP_X2]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P2 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y2]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P3 PIP X1
    $(document).on("keyup", "input[name^=HardWare_PIP_X3]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P3 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y3]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P4 PIP X1
    $(document).on("keyup", "input[name^=HardWare_PIP_X4]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P4 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y4]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P5 PIP X1
    $(document).on("keyup", "input[name^=HardWare_PIP_X5]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P5 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y5]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P6 PIP X1
    $(document).on("keyup", "input[name^=HardWare_PIP_X6]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P6 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y6]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P7 PIP X1
    $(document).on("keyup", "input[name^=HardWare_PIP_X7]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P7 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y7]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

    //P8 PIP X1
    $(document).on("keyup", "input[name^=HardWare_PIP_X8]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });
    //P8 PIP Y1
    $(document).on("keyup", "input[name^=HardWare_PIP_Y8]", function() {
    var val= $(this).val();

    if(val < -20 || val > 20) {
        alert("-20~20 범위로 입력해 주십시오.");
        $(this).val('');
    }
    });

}
