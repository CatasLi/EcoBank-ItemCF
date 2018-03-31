var exec = require('child_process').exec;
var filename = 'ItemCF2.py'
var user="022079f406ed72713a1de80e7da7c9b9";
var K=60;
var RN=10;
exec('python'+' '+filename+' '+user+' '+K+' '+RN,function(err,stdout,stderr){
    if(err)
    {
        console.log('stderr',err);
    }
    if(stdout)
    {
        //console.log(stdout);
		obj = JSON.parse(stdout);
		for(var key in obj){
			console.log(key,obj[key])
		}
    }
});