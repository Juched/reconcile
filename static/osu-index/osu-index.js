import {LitElement} from '../node_modules/lit-element/lit-element.js'
import {customElement} from '../node_modules/@lit/reactive-element/decorators/custom-element.js'
import {html} from '../node_modules/lit-html/lit-html.js'
import {css} from '../node_modules/@lit/reactive-element/css-tag.js'
import {ReceiptButton } from '../receipt-button/receipt-button.js'
const primary = css`#CFCCD6`;
const secondary = css`#4C6085`;
const tertiary = css`#49A078`;
const quaternary = css`#E85D75`;
const quinternary = css`#F39237`;

export class OsuIndex extends LitElement {
  static get styles() {
    
    return css` 

    .container {
      display: flex;
      height: 100%;
    }
    .card {
      background-color: ${secondary};
      border: 2px solid ${quinternary};
      border-radius: 9px;
      margin: 5px;
      padding: 5px;
    }
    
    @import url("https://fonts.googleapis.com/css?family=Nova+Mono&display=swap");
    * {
      box-sizing: border-box;
      padding: 0;
      margin: 0;
    }

    `;
  }

  static get properties() {
    return {
      name: {type: String},
      receipts: {type: Array}
    }
  }

  constructor() {
    super();  

    
  }

  /* TODO do update of all receipts button */
  receiptsUpdate(){

  }

  async firstUpdated() {
    // Give the browser a chance to paint
    await new Promise((r) => setTimeout(r, 5));

    var shadowRoot = this.shadowRoot;
    var that = this
    $.ajax({
      type: "GET",
      url: "/api/v1/receipts",
      timeout: 600000,
      success: function (data) {
          console.log(data);
          that.receipts = data
          that.receiptsUpdate()
      },
    });


    this.shadowRoot.querySelector("#btnSubmit").addEventListener("click", function (event) {
      event.preventDefault();
      var form = shadowRoot.querySelector('form');
      var data = new FormData(form);
      
      data.append('file', shadowRoot.querySelectorAll('input[type=file]')[0].files[0]);
      //shadowRoot.querySelector("#btnSubmit").prop("disabled", true);
      $.ajax({
          type: "POST",
          enctype: 'multipart/form-data',
          url: "/api/v1/read",
          data: data,
          processData: false,
          contentType: false,
          cache: false,
          timeout: 600000,
          success: function (data) {
              console.log();
          },
      });
    });
  }
  
  

  render() {
    var shekwes = "yeah i'm shekwes"
    return html`
    <div>    
    <receipt-button name="${shekwes}"></receipt-button>
    <form method="post" enctype="multipart/form-data">
      <input id="myFileInput" type="file" accept="image/*;capture=camera">
      <input id="btnSubmit" type="submit">
    </form>

    


    </div>`;
  }

  // VARIABLES ―――――――――――――――――――――――――
  updated(changedProperties) {
  
  
  }
}
customElements.define('osu-index', OsuIndex);
