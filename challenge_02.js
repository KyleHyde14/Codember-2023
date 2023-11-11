let decode = (secret) => {
    let init = 0;
    let ans = ''
    for (i of secret){
        if (i == '#'){
            init += 1
        } else if (i == '@'){
            init -= 1
        } else if (i == '*'){
            init *= init
        } else {
            ans += init.toString()
        }
    }

    return ans
}

let secret = '&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&'
console.log(decode(secret))