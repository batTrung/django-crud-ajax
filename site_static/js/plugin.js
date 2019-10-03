$(function(){
    // Select/Deselect checkboxes
    $("#selectAll").click(function(){
        var checkbox = $('table tbody input[type="checkbox"]');
        if(this.checked){
            checkbox.each(function(){
                this.checked = true;                  
            });
        } else{
            checkbox.each(function(){
                this.checked = false;                        
            });
        } 
    });
    
    $('tbody').on('click', 'input[type="checkbox"]', function(){
        if (!this.checked){
            $("#selectAll").prop("checked", false);
        }
        var checked = $('table tbody input[type="checkbox"]').not(':checked');
        if (checked.length == 0){
            $("#selectAll").prop("checked", true);
        }
    })

});