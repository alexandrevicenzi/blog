---
title: Donate
date: 2020-02-09
slug: donate
disable_comments: true
disable_share: true
description: Donate as a sign of appreciation
summary: Donations for my contributions are always welcome, but if you can contribute back to the open source community is even better.
---

Donations for my contributions are always welcome, but if you can contribute back to the open source community is even better.

This blog currently has no ads and I intend to keep this way. Most of the code that I write is under an OSS license, and my writings are usually licensed under Creative Common.

You can find multiple ways to donate below, or you can also pay me a beer, pale lager (Pilsner or Helles) preferably,  if we ever meet one day.

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
    'BTC': {
      'addr': '37Md5HiS5Qad84ryY4f5GpuUCod5hNxgqd',
      'name': 'Bitcoin',
    },
    'ETH': {
      'addr': '0x6b8AD41572dB6e2C91F314d4c4df997da1b062Bc',
      'name': 'Ethereum',
    },
    'LTC': {
      'addr': 'MWGq2vY976e6KmHUZ6QhafeHGiEipFBeG5',
      'name': 'Litecoin',
    },
    // 'ZEC': {
    //   'addr': 't1Sjvm8GzyeEjKD6gHQnigdXVaBaY1bf4KY',
    //   'name': 'Zcash',
    // },
    // 'XTZ': {
    //   'addr': 'tz1UQRC651A91cAHy4bhuwJfEFUdEmmrtUUH',
    //   'name': 'Tezos',
    // },
    // 'DOGE': {
    //   'addr': 'DKj7XRoeiHuf4TTjoRHpBBLsGR8MWA6nhA',
    //   'name': 'Dogecoin',
    // },
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
    document.getElementById('coin-alert').innerText = 'Send only {0} to this address'.format(coin);
    document.getElementById('coin-addr').innerText = addr.addr;
    document.getElementById('coin-qr').src = '/images/donate/{0}-qr.png'.format(coin.toLowerCase());
  }

  document.addEventListener('DOMContentLoaded', populate);
</script>
