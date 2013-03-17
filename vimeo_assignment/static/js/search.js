$(document).ready(function(){
    $(".search > form").submit(function(){
        ajax_request($(this).attr("action"));
        return false;
    });

    $(".filter  a").click(function(){
        all_elem = $(".filter a[href='all']");
        if($(this).is(all_elem)){
            if($(this).hasClass("active")){
                $(".filter a").removeClass("active");
            }
            else{
                $(".filter a").addClass("active");
            }
        }
        else{
            if($(this).hasClass("active")){
                $(this).removeClass("active");
                $(all_elem).removeClass("active");
            }
            else{
                $(this).addClass("active");
                if($(".filter a.active").length >= 3){
                    $(".filter a").addClass("active");
                }
            }
        }

        ajax_request($(".search > form").attr("action"));
        return false;
    });
})

function ajax_request(url){
    var search_term = $(".search input[type='text']").val();
    data = {search: search_term};
    if($(".filter a[href='paying']").hasClass("active")){
        data["paying"] = true;
    }
    if($(".filter a[href='staffpick']").hasClass("active")){
        data["staffpick"] = true;
    }
    if($(".filter a[href='uploaded']").hasClass("active")){
        data["uploaded"] = true;
    }
    $.ajax({
        url: url,
        dataType: "html",
        data:data,
        success: function(data){
            $(".results").html(data);
        }
    });
}