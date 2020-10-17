---
title: Donate
date: 2020-02-09
slug: donate
disable_comments: true
disable_share: true
description: Donate as a sign of appreciation for my contributions
---

Donations for my contributions are always welcome, but if you can contribute back to the open-source community is even better.
<!--more-->
This blog currently has no ads, and I intend to keep this way. Most of the code that I write is under a FOSS license, and my writings are usually licensed under Creative Commons.

You can find many ways to donate below, or you can also pay me a beer, pale lager (Pilsner or Helles), if we ever meet one day.

<div class="donations">
  <table class="buttons">
    <tr id="addr-buttons"></tr>
  </table>

  <table class="addr">
    <tr>
      <td id="coin-info"></td>
    </tr>
    <tr>
      <td id="coin-addr"></td>
    </tr>
    <tr>
      <td>
        <img id="coin-qr" src="">
      </td>
    </tr>
    <tr>
      <td id="coin-alert"></td>
    </tr>
  </table>
</div>

<script type="text/javascript">
  if (!String.prototype.format) {
    String.prototype.format = function() {
      var args = arguments;
      return this.replace(/{(\d+)}/g, function(match, number) { 
        return typeof args[number] != 'undefined'
          ? args[number]
          : match
        ;
      });
    };
  }

  var addrs = {
    // Coinomi
    'BTC': {
      'addr': '37Md5HiS5Qad84ryY4f5GpuUCod5hNxgqd',
      'name': 'Bitcoin',
      'multi': false,
    },
    // MyEtherWallet
    'ETH': {
      'addr': '0x8b16354C893100Eea5507AC888Cae62Ca9684c1D',
      'name': 'Ethereum',
      'token': 'ERC-20',
      'multi': true,
    },
    'PayPal': {
      'external': 'https://www.paypal.me/avicenzi'
    },
  };

  function populate() {
    tr = document.getElementById('addr-buttons');

    Object.keys(addrs).forEach(function (coin) {
      var addr = addrs[coin];


      var th = document.createElement("th");
      var a = document.createElement("a");
      var img = document.createElement("img");

      if (addr.external) {
        a.href = addr.external;
        a.target = '_blank';
      } else {
        a.href = 'javascript:void()'
        a.onclick = function() { showAddr(this.title); };
      }

      a.title = coin;

      img.src = '/images/donate/{0}.png'.format(coin.toLowerCase());
      img.className = 'coin';
      img.alt = coin;

      a.appendChild(img);
      th.appendChild(a);
      tr.appendChild(th);
    });
  }

  function showAddr(coin){
    var addr = addrs[coin];

    document.getElementById('coin-info').innerText = '{0} Address ({1})'.format(addr.name, coin);

    if (addr.multi === true) {
      document.getElementById('coin-alert').innerText = 'Send {0} or any {1} token to this address'.format(coin, addr.token);
    } else {
      document.getElementById('coin-alert').innerText = 'Send only {0} to this address'.format(coin);
    }

    document.getElementById('coin-addr').innerText = addr.addr;
    document.getElementById('coin-qr').src = '/images/donate/{0}-qr.png'.format(coin.toLowerCase());
  }

  document.addEventListener('DOMContentLoaded', populate);
</script>
