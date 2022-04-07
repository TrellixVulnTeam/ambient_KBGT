(
MIDIClient.init;

MIDIIn.connectAll;

MIDIFunc.trace(true);
)
(
/*SynthDef(\sin, {
	arg freq=200, harm=8, amp=0.1, out=0;
	var sig, env;
	sig = {SinOsc.ar(freq * Rand(-0.2, 0.2).midiratio)}!2;
	sig = Splay.ar(sig);
	sig = sig * 10;
	sig = sig.softclip;
	sig = RLPF.ar(sig, (freq * harm).clip(20,20000), 0.9);
	env = EnvGen.ar(Env.sine(dur: 4.5, level: 0.4), doneAction:2);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;*/

SynthDef(\perc, {
	arg freq=200, harm=8, amp=0.1, out=0;
	var sig, env;
	sig = {SinOsc.ar(freq * Rand(-0.2, 0.2).midiratio)}!2;
	sig = Splay.ar(sig);
	sig = RLPF.ar(sig, (freq * harm).clip(20,20000), 0.5);
	env = EnvGen.ar(Env.perc(0.01, 0.8, 0.65), doneAction:2);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;

/*MIDIdef.noteOn(\on, {
	arg val, num, chan, src;
	Synth(\sin, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
});*/

MIDIdef.noteOn(\on, {
	arg val, num, chan, src;
	Synth(\perc, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
});

/*MIDIdef.noteOff(\off, {
	Synth(\sin, [
		\gate, 0
	]);
});*/

MIDIdef.noteOff(\off, {
	Synth(\perc, [
		\gate, 0
	]);
});
)