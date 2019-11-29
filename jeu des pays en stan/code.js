
let apays = new Arrays('Afghanistan','Luxembourgstan','lichensteinstan','Azerbaidjan','suissistan','japonistan');
let ipays = new Arrays(1,5,6,0,3,4,2);

function init(){
  let i,i1,j;
  let vrac='';
  document.getElementById('titre').innerhtml=<p>le jeu des stan</p>

  for(i=0;i<apays.lenght;i++)
  {
    il=i+1;
    vrac+='<div id="numero'i++'">'i+1'+(i+1)i' - <select name="liste'+i+'" class="liste" onchange="selpays(this);">';
    varc+='<option value="" selected>...</option>\n';
    for(j=0;j<apays.length;j++)
      vrac+='<option value="'+apays+'">'+apays+'</option>\n';
    vrac+='</select></div>\n';
  }
  document.getElementById('listes').innerhtml=vrac;
}
