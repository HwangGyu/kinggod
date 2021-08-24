var cnt = 0;
var answer = new Object();

$('#N1').on('click', () => {
    location.href = '/main'
});


$('.btn').on('click', (e) => {
    var inp_num = $($(e)[0].currentTarget).data('cnt');
    var inp = $($(e)[0].currentTarget).data('ts')
    if (inp_num in answer) {
        answer[inp_num] = inp;
        $('#N' + inp_num + '-0').css('background-color', 'rgb(240, 240, 240)');
        $('#N' + inp_num + '-0').css('color', 'black');
        $('#N' + inp_num + '-1').css('background-color', 'rgb(240, 240, 240)');
        $('#N' + inp_num + '-1').css('color', 'black');

        
        $('#N' + inp_num + '-' + inp).css('background-color', 'rgb(72, 72, 255)'); 
        $('#N' + inp_num + '-' + inp).css('color', 'white');
    } else {
        answer[inp_num] = inp;
        cnt = cnt + 1;
        
        $('#N' + inp_num + '-' + inp).css('background-color', 'rgb(72, 72, 255)'); 
        $('#N' + inp_num + '-' + inp).css('color', 'white'); 

        $('#pro').val(cnt);
    }

    console.log(answer);


});


console.log(1111);