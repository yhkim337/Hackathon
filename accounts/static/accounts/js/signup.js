const idDuplicateCheck = async () => {
    const username = getUsername();
    if(username){
        const data = new FormData();
        data.append("content", username);
        const response = await axios.post(`/accounts/signup/check/`, data);
        console.log(response.data.duplicate)
        const duplicate = response.data.duplicate;
        if (duplicate === "pass"){
            const isDuplicate = document.getElementById('isDuplicate')
            isDuplicate.innerHTML = '사용이 가능합니다'
            isDuplicate.style.color = 'green'
        } else{
            const isDuplicate = document.getElementById('isDuplicate')
            isDuplicate.innerHTML = '사용이 불가능합니다'
            isDuplicate.style.color = 'red'
        }
    }
};

const signupForm = document.getElementById('signup-form');

signupForm.onsubmit = (e) => handleSignup(e);

const handleSignup = (e) => {
	e.preventDefault();
	username = getUsername();
	passwords = getPasswords();

	if (validateUsername(username) && validatePassword(passwords)) {
		submitTarget(e);
	} else {
        showErrorModal();
	}
};

const getUsername = () => {
	return document.querySelector('input[name=username]').value;
};

const validateUsername = (username) => {
	return username !== '';
};

const getPasswords = () => {
	return [...document.querySelectorAll('input[type=password]')].map(
		(input) => input.value
	);
};

const isSamePassword = ([pw1, pw2]) => {
	return pw1 === pw2;
};

const validatePassword = (passwords) => {
	return isSamePassword(passwords) && isValidFormatPassword(passwords);
};

const isValidFormatPassword = ([pw]) => {
	const regExp = /^[A-Za-z0-9]{3,}$/;

	return regExp.test(pw);
};

const submitTarget = (e) => {
	e.target.submit();
};

const showErrorModal = () => {
	var myModal = new bootstrap.Modal(document.getElementById('exampleModal'))
    myModal.show();
};


const inputTags = [...document.querySelectorAll('input')];

const disableInputTags = () => {
	inputTags.forEach((inputTag) => (inputTag.disabled = true));
};

const enableInputTags = () => {
	inputTags.forEach((inputTags) => (inputTags.disabled = false));
};