const readline = require('readline');

const rl = readline.createInterface(process.stdin,process.stdout);

rl.setPrompt('Enter a new ID(A123??6789)> ');
rl.prompt();

rl.on('line', (line) => {
	if(/[A-Za-z\?][12\?][0-9\?]{8}/.test(line)){
		const id = line.toUpperCase();
		const arr = [];
		const dict = {
			A: 10, B: 11, C: 12, D: 13, E: 14, F: 15, G: 16, H: 17, I: 34,
			J: 18, K: 19, L: 20, M: 21, N: 22, O: 35, P: 23, Q: 24, R: 25,
			S: 26, T: 27, U: 28, V: 29, W: 32, X: 30, Y: 31, Z: 33
		};
		arr[0] = dict[id[0]];
		Object.keys(id).forEach((i) => {
			if( i>= 1 && /[0-9]/.test(id[i])){
				arr[i] = ~~id[i];
			}
		});

		let checkSum = arr[0] ? ~~(arr[0] / 10) + arr[0] % 10 * 9 : 0;
		Object.keys(arr).forEach((i) => {
			if( i >= 1 && arr[i] >= 0) checkSum += (9-i > 0 ? 9-i : 1) * arr[i];
		});

		if(arr.filter(x => x >= 0).length === 10){
			if(checkSum % 10 === 0){
				console.log('real');
			}else{
				console.log('fake');
			}
		}else{
			const oldCheckSum = checkSum;
			let maskCount = 10;
			Object.keys(arr).forEach((i) => {
				if(arr[i]>=0) maskCount--;
			})
			console.log('possible IDs:');
			if(arr[0]){
				for(let i=0;i<Math.pow(10, maskCount);i++){
					const session = Array.from(`${i}`).map(x => ~~x);
					while(session.length < maskCount) session.unshift(0);
					checkSum = oldCheckSum;
					let k = 0;
					for(let j=0;j<10;j++){
						if(!(arr[j]>=0)){
							checkSum += (9-j > 0 ? 9-j : 1) * session[k];
							k++;
						}
					}
					if(checkSum % 10 === 0){
						k=0;
						let str = id[0];
						for(let j=1;j<10;j++){
							str += (arr[j] >= 0 ? arr[j] : session[k++]);
						}
						if(/[A-Za-z][12][0-9]{8}/.test(str))console.log(str);
					}
				}
			}else{
				for(let m=0;m<26;m++){
					arr[0] = dict[String.fromCharCode(65 + m)];
					for(let i=0;i<Math.pow(10, maskCount-1);i++){
						const session = Array.from(`${i}`).map(x => ~~x);
						while(session.length < maskCount-1) session.unshift(0);
						checkSum = oldCheckSum + ~~(arr[0] / 10) + arr[0] % 10 * 9;
						let k = 0;
						for(let j=0;j<10;j++){
							if(!(arr[j]>=0)){
								checkSum += (9-j > 0 ? 9-j : 1) * session[k];
								k++;
							}
						}
						if(checkSum % 10 === 0){
							k=0;
							let str = String.fromCharCode(65 + m);
							for(let j=1;j<10;j++){
								str += (arr[j] >= 0 ? arr[j] : session[k++]);
							}
							if(/[A-Za-z][12][0-9]{8}/.test(str))console.log(str);
						}
					}
				}
			}
		}
	}else{
		console.log('wrong format.');
	}
	rl.prompt();
});
