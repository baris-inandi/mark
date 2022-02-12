html lang="en" class="dark"
  head
    meta attr charset="utf-8"
    meta .description attr name="description" content="hi"
    title
        "hello"

    require index.js
    require style.css

    style:
      .small {font-size: 0.8em;}
      .red {color: red;}
      .anotherClass {margin: 10px;}
    end

    script:
      console.log("this is js over here")
    end

  body
    div .large .button .big #submit-btn-outer
    and .anotherClass
    and attr stringAttr="value"
      button .red #submit-btn
        "Submit"
      and attr style="font-family: Inter, sans-serif;"
      p .small
        "This is a paragraph"
    div .second #second-div
