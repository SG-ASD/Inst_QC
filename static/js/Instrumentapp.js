'use strict';

/**
 * start 버튼 클릭 시 해당 장비의 모달창 생성
 */
const startModal = document.getElementById('startModal');  // 주어진 문자열과 일치하는 id 속성을 가진 요소를 찾고, 이를 나타내는 Element 객체 반환
startModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    const button = event.relatedTarget;
    // Extract info from data-bs-* attributes
    const name = button.getAttribute('data-bs-name');  // 선택한 요소의 특정 속성 값 반환
    const SN = button.getAttribute('data-SN');  // button의 data-SN 속성 값 반환
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    // querySelector() : 특정 name, id, class를 제한하지 않고 css 선택자를 사용하여 요소를 반환
    // querySelector(#section) : id=section인 요소를 반환
    // querySelector(.section) : class=section인 요소를 반환
    const instrument_name = startModal.querySelector('.text-name')
    const instrument_SN = startModal.querySelector('.text-SN')
    const instrument_inspector = startModal.querySelector('.text-inspector')
    const update_SN = startModal.querySelector('.update_SN')

    // modalTitle.textContent = 'New message to ' + recipient
    // modalBodyInput.value = name
    instrument_name.textContent = name
    instrument_SN.textContent = SN
    instrument_inspector.value = ""
    update_SN.textContent = SN
    // print()
})

/**
 * 장비 등록 엑셀파일 load
 */
function ExcelImport(Event) {
    let file = Event.target.files[0]; //input file 객체를 가져온다.
    let reader = new FileReader(); // FileReader를 생성한다.
    reader.readAsArrayBuffer(file);

    reader.onload = function () {
        let fileData = reader.result; //FileReader 결과 데이터를 가져온다.
        fileData = new Uint8Array(fileData);
        let wb = XLSX.read(fileData, {type: 'array'}); // array 형태로 엑셀파일을 읽는다.
        let sheetName = wb.SheetNames;

        let sheet_data = XLSX.utils.sheet_to_json(wb.Sheets[sheetName[0]], {header:1});

        console.log(sheet_data);
        let inst_list = []  // 배열 선언

        if(sheet_data.length > 0) {
            let table_output = '<table class="table table-striped table-bordered">';
            table_output += '<input type="hidden" name="excel_data" value="'+sheet_data+'">';

            for(let row = 0; row < sheet_data.length; row++) {
                table_output += '<tr>';
                for(let cell = 0; cell < sheet_data[row].length; cell++) {
                    if(row == 0) {  // 엑셀파일의 header
                        table_output += '<th>'+sheet_data[row][cell]+'</th>';
                    }
                    else {  // 엑셀파일의 data
                        table_output += '<td><input readonly type="text" value="'+sheet_data[row][cell]+'"></td>';
                    }
                }
                table_output += '</tr>';
            }
            table_output += '</table>';

            document.getElementById('displayExcel').innerHTML = table_output;
        }
    };
}
