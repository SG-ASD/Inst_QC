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
 * 테스트
 */
// function excelImport(Event) {
//     alert("js")
//     alert(Event.target)
//     const file = Event.target.files[0];
//     const reader = new FileReader();
//
//     reader.onload = function(){
//         const fileData = reader.result;
//         const wb = XLSX.read(fileData, {type : 'binary'});
//
//         wb.SheetNames.forEach(function(sheetName){
//             const row =XLSX.utils.sheet_to_json(wb.Sheets[sheetName]);
//             console.log(JSON.stringify(row));
//             alert(JSON.stringify(row))
//         })
//     };
//     reader.readAsBinaryString(file);
//     alert(file)
// }
