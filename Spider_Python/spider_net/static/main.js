/**
 * Created by Administrator on 2017/3/21.
 */
$(function(){
    //返回顶部
    $(".backtop").click(function(){
        $("html,body").animate({scrollTop: '0px'}, 1000);
        return false;
    });
    //筛选栏伸缩
    $(".bottom").click(function(){
        $(".fade-content").slideToggle();
        $(".content").slideToggle();
    });
    //快捷方式发送数据
    $(".fade-content .location a").click(function(){
        $(this).addClass("selected");
        $(this).parent('li.ll').siblings().find("a").removeClass("selected");
        $("input.location").val($(this).text());
        $("form").submit();
    });
    $(".fade-content .rule a").click(function(){
        $(this).addClass("selected");
        $(this).parent('li.rr').siblings().find("a").removeClass("selected");
        $("input.rule").val($(this).text());
        $("form").submit();
    });
    $(".fade-content .school a").click(function(){
        $(this).addClass("selected");
        $(this).parent('li.ss').siblings().find("a").removeClass("selected");
        $("input.school").val($(this).text());
        $("form").submit();
    });
});