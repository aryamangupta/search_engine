
    var items = [
    {
        name: '---',
        value:'',
        subitems: []
    },
    {
        name:'Banglore', 
        value: 'Banglore', 
        subitems: [
            {name: 'Lajpat Nagar', value: 'Lajpat Nagar'}, 
            {name:'Rajendra Nagar', value:'Rajendra Nagar'}
        ]
    },
    {
        name: 'Ahemdabad',
        value: 'Ahemdabad',
        subitems: [
            {name: 'Gachibowli', value:'Gachibowli'},
            {name: 'South extension', value:'South extension'}
        ]
    }
];


$(function(){
    var temp = {};

    $.each(items, function(){
        $("<option />")
        .attr("value", this.value)
        .html(this.name)
        .appendTo("#firstmenu");
        temp[this.value] = this.subitems;
    });

    $("#firstmenu").change(function(){
        var value = $(this).val();
        var menu = $("#secondmenu");

        menu.empty();
        $.each(temp[value], function(){
            $("<option />")
            .attr("value", this.value)
            .html(this.name)
            .appendTo(menu);
        });
    }).change();


});


function loadXMLDoc()
{
var a = document.getElementById("text").value;
//alert(a);	

var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("main").innerHTML=xmlhttp.responseText;
    var r = xmlhttp.responseText;
    var d = eval("(" + r + ")");
    //alert(d['names'][0]);
    }
  }
xmlhttp.open("GET","ace?key="+a,true);
xmlhttp.send();
}

