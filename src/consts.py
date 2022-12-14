ROOT = 'wss://shoutbox.cracked.io/socket.io/?token={token}&EIO=3&transport=websocket'

RANKS = {
    'supreme_rank': '53ffa1',
    'infinity_rank': 'ff84bc',
    'premium_rank': '68dbff',
    'registered_rank': 'ffffff',

    'contributor_rank': 'ffd600',
    'dev_rank': 'c61aff',
    'godlike_rank': 'e33dcd',
    'heaven_rank': 'c8378d',
    'reverser_rank': '8ee5e2',
    'coder_rank': 'a868ed',
    'disinfector_rank': '7b9dff',

    'admin_rank': 'D8185C',
    'mods_rank': 'ed7a16',
    'trial_mod_rank': '028e6b'
}
SMILIES = {
    ':monkas:': 'https://static.cracked.io/images/smilies/monkas.png',
    ':monkah:': 'https://static.cracked.io/images/smilies/monkah.png',
    ':pepe:': 'https://static.cracked.io/images/smilies/pepe.gif',
    ':feelssadman:': 'https://static.cracked.io/images/smilies/feelssadman.png',
    ':pepi:': 'https://static.cracked.io/images/smilies/pepi.png',
    ':kek:': 'https://static.cracked.io/images/smilies/kek.png',
    ':hackerman:': 'https://static.cracked.io/images/smilies/hackerman.gif',
    ':sheepe:': 'https://static.cracked.io/images/smilies/sheepe.gif',
    ':weebsout:': 'https://static.cracked.io/images/smilies/weebsout.png',
    ':ban2:': 'https://static.cracked.io/images/smilies/ban2.gif',
    ':pepeglad:': 'https://static.cracked.io/images/smilies/pepeglad.png',
    ':pepeknife:': 'https://static.cracked.io/images/smilies/pepeknife.png',
    ':peperee:': 'https://static.cracked.io/images/smilies/peperee.png',
    ':pepecaught:': 'https://static.cracked.io/images/smilies/pepecaught.gif',
    ':sleepingpepe:': 'https://static.cracked.io/images/smilies/sleep.png',
    ':pepeokay:': 'https://static.cracked.io/images/smilies/pepeokay.png',
    ':bdsm:': 'https://static.cracked.io/images/smilies/bdsm.png',
    ':popcorn:': 'https://static.cracked.io/images/smilies/popcorn2.gif',
    ':music:': 'https://static.cracked.io/images/smilies/PepeMusic2.gif',
    ':pepo:': 'https://static.cracked.io/images/smilies/pepo.png',
    ':box:': 'https://static.cracked.io/images/smilies/box.gif',
    ':wack:': 'https://static.cracked.io/images/smilies/wack.png',
    ':lol2:': 'https://static.cracked.io/images/smilies/lol2.gif',
    ':multiriot:': 'https://static.cracked.io/images/smilies/riot2.gif',
    ':monkayes:': 'https://static.cracked.io/images/smilies/monkayes.gif',
    ':clown:': 'https://static.cracked.io/images/smilies/clown2.gif',
    ':blush:': 'https://static.cracked.io/images/smilies/PepeBlush.png',
    ':smart:': 'https://static.cracked.io/images/smilies/smart.gif',
    ':wash:': 'https://static.cracked.io/images/smilies/wash.gif',
    ':hang:': 'https://static.cracked.io/images/smilies/hang.gif',
    ':??:': 'https://static.cracked.io/images/smilies/who.png',
    ':hype:': 'https://static.cracked.io/images/smilies/hype.png',
    ':drive:': 'https://static.cracked.io/images/smilies/drive.gif',
    ':pepejail:': 'https://static.cracked.io/images/smilies/pepejail.gif',
    ':pepesad:': 'https://static.cracked.io/images/smilies/pepesadheart.png',
    ':sabers:': 'https://static.cracked.io/images/smilies/sabers.gif',
    ':wut:': 'https://static.cracked.io/images/smilies/wut.png',
    ':saddance:': 'https://static.cracked.io/images/smilies/dance3.gif',
    ':hide:': 'https://static.cracked.io/images/smilies/hide.gif',
    ':stalk:': 'https://static.cracked.io/images/smilies/stalk.gif',
    ':police:': 'https://static.cracked.io/images/smilies/police.png',
    ':fiesta2:': 'https://static.cracked.io/images/smilies/fiesta.gif',
    ':no:': 'https://static.cracked.io/images/smilies/no.png',
    ':yes:': 'https://static.cracked.io/images/smilies/yes.png',
    ':heart:': 'https://static.cracked.io/images/smilies/heart5.png',
    ':door:': 'https://static.cracked.io/images/smilies/door2.gif',
    ':mad:': 'https://static.cracked.io/images/smilies/mad.png',
    ':cry:': 'https://static.cracked.io/images/smilies/cryfloor.png',
    ':pepelove:': 'https://static.cracked.io/images/smilies/pepelove.png',
    ':pepeclap:': 'https://static.cracked.io/images/smilies/pepeclap2.gif',
    ':feelsstrongnan:': 'https://static.cracked.io/images/smilies/FeelsStrongMan.png',
    ':ughpepe:': 'https://static.cracked.io/images/smilies/ughpepe.png',
    ':pepothink:': 'https://static.cracked.io/images/smilies/PepoThink.png',
    ':maam:': 'https://static.cracked.io/images/smilies/maam.gif',
    ':kappa:': 'https://static.cracked.io/images/smilies/kappa.png',
    ':badcat:': 'https://static.cracked.io/images/smilies/badcat.gif',
    ':woow:': 'https://static.cracked.io/images/smilies/wooow.png',
    ':thinkingpepe:': 'https://static.cracked.io/images/smilies/thinkingpepe.png',
    ':poggershype:': 'https://static.cracked.io/images/smilies/PoggersHype.gif',
    ':pepemusic:': 'https://static.cracked.io/images/smilies/pepemusic.gif',
    ':kingpepo:': 'https://static.cracked.io/images/smilies/pepo2.png',
    ':mlg:': 'https://static.cracked.io/images/smilies/MLGpepe.png',
    ':pepeteddy:': 'https://static.cracked.io/images/smilies/PepeTeddy.gif',
    ':pepecrab:': 'https://static.cracked.io/images/smilies/pepecrab.gif',
    ':icecream:': 'https://static.cracked.io/images/smilies/icecream.gif',
    ':coffee:': 'https://static.cracked.io/images/smilies/coffe.gif',
    ':jam2:': 'https://static.cracked.io/images/smilies/jam2.gif',
    ':riot:': 'https://static.cracked.io/images/smilies/riot.gif',
    ':bye:': 'https://static.cracked.io/images/smilies/bye3.gif',
    ':fart:': 'https://static.cracked.io/images/smilies/fart.gif',
    ':goose:': 'https://static.cracked.io/images/smilies/goose.gif',
    ':why:': 'https://static.cracked.io/images/smilies/why.gif',
    ':noob:': 'https://static.cracked.io/images/smilies/noob.gif',
    ':scam:': 'https://static.cracked.io/images/smilies/scam.gif',
    ':kiss:': 'https://static.cracked.io/images/smilies/kiss.gif',
    ':gib:': 'https://static.cracked.io/images/smilies/gib.png',
    ':clown2:': 'https://static.cracked.io/images/smilies/clown.gif',
    ':spin:': 'https://static.cracked.io/images/smilies/spin.gif',
    ':lol:': 'https://static.cracked.io/images/smilies/lol.gif',
    ':ban:': 'https://static.cracked.io/images/smilies/ban.gif',
    ':hammer:': 'https://static.cracked.io/images/smilies/FeelsBanMan.png',
    ':hammer2:': 'https://static.cracked.io/images/smilies/hammer2.gif',
    ':denmark:': 'https://static.cracked.io/images/smilies/bruh.gif',
    ':evil:': 'https://static.cracked.io/images/smilies/evilrondo.png',
    ':butler:': 'https://static.cracked.io/images/smilies/buttler.png',
    ':tos:': 'https://static.cracked.io/images/smilies/tos.gif',
    ':shrug:': 'https://static.cracked.io/images/smilies/shrug.gif',
    ':pizza:': 'https://static.cracked.io/images/smilies/pizza.gif',
    ':angry:': 'https://static.cracked.io/images/smilies/meangry.gif',
    ':pissed:': 'https://static.cracked.io/images/smilies/pissed.gif',
    ':salami:': 'https://static.cracked.io/images/smilies/salami.gif',
    ':salami2:': 'https://static.cracked.io/images/smilies/salami2.gif',
    ':catree:': 'https://static.cracked.io/images/smilies/catree.png',
    ':coffin:': 'https://static.cracked.io/images/smilies/coffin.gif',
    ':wine:': 'https://static.cracked.io/images/smilies/pepowine.gif',
    ':suit:': 'https://static.cracked.io/images/smilies/suit.png',
    ':pepechair:': 'https://static.cracked.io/images/smilies/pepechair.gif',
    ':topkek:': 'https://static.cracked.io/images/smilies/topkek.gif',
    ':fat:': 'https://static.cracked.io/images/smilies/fat.gif',
    ':bonk:': 'https://static.cracked.io/images/smilies/bonk.gif',
    ':shake:': 'https://static.cracked.io/images/smilies/shake.gif',
    ':ricardo:': 'https://static.cracked.io/images/smilies/ricardo.gif',
    ':hyperneko:': 'https://static.cracked.io/images/smilies/hyperneko.gif',
    ':multikek:': 'https://static.cracked.io/images/smilies/multikek.gif',
    ':keeksad:': 'https://static.cracked.io/images/smilies/keeksad.png',
    ':keek:': 'https://static.cracked.io/images/smilies/keek.gif',
    ':sadnigga:': 'https://static.cracked.io/images/smilies/sadnigga.png',
    ':fbi:': 'https://static.cracked.io/images/smilies/fbi.gif',
    ':dorime:': 'https://static.cracked.io/images/smilies/dorime.png',
    ':smoke:': 'https://static.cracked.io/images/smilies/smoke.gif',
    ':facts:': 'https://static.cracked.io/images/smilies/facts.gif',
    ':sadnigga2:': 'https://static.cracked.io/images/smilies/sadnigga.gif',
    ':???:': 'https://static.cracked.io/images/smilies/what_.gif',
    ':serioushabibi:': 'https://static.cracked.io/images/smilies/habibi.png',
    ':run:': 'https://static.cracked.io/images/smilies/run.gif',
    ':awkward:': 'https://static.cracked.io/images/smilies/awkward.gif',
    ':bear:': 'https://static.cracked.io/images/smilies/bear.gif',
    ':ksz:': 'https://static.cracked.io/images/smilies/ksz.png',
    ':10:': 'https://static.cracked.io/images/smilies/10.png',
    ':heyguys:': 'https://static.cracked.io/images/smilies/heyguys.png',
    ':jew:': 'https://static.cracked.io/images/smilies/jewl.gif',
    ':ksz2:': 'https://static.cracked.io/images/smilies/ksz2.png',
    ':fatcat:': 'https://static.cracked.io/images/smilies/fatcat.png',
    ':money:': 'https://static.cracked.io/images/smilies/florain.gif',
    ':pogchamp:': 'https://static.cracked.io/images/smilies/pogchamp.png',
    ':fappa:': 'https://static.cracked.io/images/smilies/fappa.png',
    ':amusing:': 'https://static.cracked.io/images/smilies/Amusing.png',
    ':dead:': 'https://static.cracked.io/images/smilies/dead.png',
    ':klappa:': 'https://static.cracked.io/images/smilies/klappa.png',
    ':dingdong:': 'https://static.cracked.io/images/smilies/dingdong.gif',
    ':thinking:': 'https://static.cracked.io/images/smilies/thinking.png',
    ':feelsabdulman:': 'https://static.cracked.io/images/smilies/feelsabdulman.gif',
    ':angrydog:': 'https://static.cracked.io/images/smilies/angrydoggo.png',
    ':really:': 'https://static.cracked.io/images/smilies/really.png',
    ':nooo:': 'https://static.cracked.io/images/smilies/nooo.gif',
    ':cool:': 'https://static.cracked.io/images/smilies/cooldog.gif',
    ':banana:': 'https://static.cracked.io/images/smilies/banana.gif',
    ':wow:': 'https://static.cracked.io/images/smilies/wow.gif',
    ':happyhabibi:': 'https://static.cracked.io/images/smilies/happyhabibi.png',
    ':uwu:': 'https://static.cracked.io/images/smilies/jiggly.gif',
    ':cheemsbonk:': 'https://static.cracked.io/images/smilies/cheemsbonk.gif',
    ':weed:': 'https://static.cracked.io/images/smilies/weed.gif',
    ':zaida:': 'https://static.cracked.io/images/smilies/zaida.jpg',
    ':patpat:': 'https://static.cracked.io/images/smilies/patpatsadlove.gif',
    ':catjam:': 'https://static.cracked.io/images/smilies/catjam.gif',
    ':facepalm:': 'https://static.cracked.io/images/smilies/facepalm.png',
    ':omg:': 'https://static.cracked.io/images/smilies/omg2.gif',
    ':happy:': 'https://static.cracked.io/images/smilies/happy.png',
    ':dog:': 'https://static.cracked.io/images/smilies/dog.gif',
    ':darkness:': 'https://static.cracked.io/images/smilies/darkness3.png',
    ':hans:': 'https://static.cracked.io/images/smilies/handsome.png',
    ':hans2:': 'https://static.cracked.io/images/smilies/handsome.gif',
    ':type:': 'https://static.cracked.io/images/smilies/type.gif',
    ':thief:': 'https://static.cracked.io/images/smilies/thief2.gif',
    ':patbear:': 'https://static.cracked.io/images/smilies/bearpat.gif',
    ':smokingnigga:': 'https://static.cracked.io/images/smilies/smokingnigga.png',
    ':popcat:': 'https://static.cracked.io/images/smilies/popcat.gif',
    ':wtf:': 'https://static.cracked.io/images/smilies/wtf.png',
    ':rip:': 'https://static.cracked.io/images/smilies/rip.png',
    ':budget:': 'https://static.cracked.io/images/smilies/hyped2.gif',
    ':haha:': 'https://static.cracked.io/images/smilies/haha2.png',
    ':cook:': 'https://static.cracked.io/images/smilies/cook.gif',
    ':pray:': 'https://static.cracked.io/images/smilies/pray2.png',
    ':gun:': 'https://static.cracked.io/images/smilies/gun.gif',
    ':dance2:': 'https://static.cracked.io/images/smilies/dance4.gif',
    ':sus:': 'https://static.cracked.io/images/smilies/sus.png',
    ':mesvak2:': 'https://static.cracked.io/images/smilies/mesvak.gif',
    ':ohwaitno:': 'https://static.cracked.io/images/smilies/ohwaitno.gif',
    ':clown3:': 'https://static.cracked.io/images/smilies/clown3.gif',
    ':lawyer:': 'https://static.cracked.io/images/smilies/lawyer.png',
    ':pepesmoke2:': 'https://static.cracked.io/images/smilies/pepesmoke3.gif',
    ':daddy:': 'https://static.cracked.io/images/smilies/daddy.gif',
    ':ang:': 'https://static.cracked.io/images/smilies/ang.png',
    ':confused:': 'https://static.cracked.io/images/smilies/confused.gif',
    ':toof:': 'https://static.cracked.io/images/smilies/toof5.gif',
    ':nigger:': 'https://static.cracked.io/images/smilies/pepenigger.gif',
    ':niggalo:': 'https://static.cracked.io/images/smilies/pepeniggalo.gif',
    ':feelsamazingman:': 'https://static.cracked.io/images/smilies/feelsamazingman.png',
    ':kekg:': 'https://static.cracked.io/images/smilies/kekgold.gif',
    ':goldnigga:': 'https://static.cracked.io/images/smilies/goldnigga.gif',
    ':chatting:': 'https://static.cracked.io/images/smilies/chatting.gif',
    ':mesvak:': 'https://static.cracked.io/images/smilies/mesvak2.png',
    ':witch:': 'https://static.cracked.io/images/smilies/witch2.gif',
    ':evilpat:': 'https://static.cracked.io/images/smilies/patevil.gif',
    ':hellohabibi:': 'https://static.cracked.io/images/smilies/hihabibi.png',
    ':communist:': 'https://static.cracked.io/images/smilies/communism2.png',
    ':dance:': 'https://static.cracked.io/images/smilies/dancing_kid.gif',
    ':kap:': 'https://static.cracked.io/images/smilies/kap.png',
    ':lulz:': 'https://static.cracked.io/images/smilies/lul.gif',
    ':salamilove:': 'https://static.cracked.io/images/smilies/salamilove2.gif',
    ':pepef:': 'https://static.cracked.io/images/smilies/pepef.png',
    ':donut:': 'https://static.cracked.io/images/smilies/donut.png',
    ':gigachad:': 'https://static.cracked.io/images/smilies/gigachad.png',
    ':fiesta:': 'https://static.cracked.io/images/smilies/fiesta4.gif',
    ':openup:': 'https://static.cracked.io/images/smilies/openup.gif',
    ':slave:': 'https://static.cracked.io/images/smilies/slave1.gif',
    ':arrive:': 'https://static.cracked.io/images/smilies/arrive.gif',
    ':broke:': 'https://static.cracked.io/images/smilies/broke.gif',
    ':usa:': 'https://static.cracked.io/images/smilies/usa.gif',
    ':monkey:': 'https://static.cracked.io/images/smilies/monkey.gif',
    ':ok:': 'https://static.cracked.io/images/smilies/ok.gif',
    ':budgetfiesta:': 'https://static.cracked.io/images/smilies/fiesta_parrot.gif',
    ':budgetrub:': 'https://static.cracked.io/images/smilies/birdman.gif'
}
