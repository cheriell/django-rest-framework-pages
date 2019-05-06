function validateForm() {
    var fail = '';

    var years_musical_training = document.forms['user-study']['years_musical_training'].value;
    var name = document.forms['user-study']['name'].value;

    if(years_musical_training == '') {
        fail += 'Please fill in your years of musical training\n';
    }
    if(name == '') {
        fail += 'Please fill in your name\n';
    }

    if(fail == '') {
        return true;
    } else {
        alert(fail);
        return false;
    }
}