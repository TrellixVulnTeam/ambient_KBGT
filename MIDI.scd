(
MIDIClient.init;

MIDIIn.connectAll;

MIDIFunc.trace(true);
)
(
SynthDef(\sin, {
	arg freq, harm=4, amp=0.1, out=0;
	var sig, env;
	sig = {SinOsc.ar(freq * Rand(-0.2, 0.2).midiratio)}!2;
	sig = Splay.ar(sig);
	sig = sig * 3;
	sig = sig.softclip;
	sig = RLPF.ar(sig, (freq * harm).clip(20,20000), 0.5);
	env = EnvGen.ar(Env.sine(dur: 4.5, level: 0.4), doneAction:2);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;

SynthDef(\perc, {
	arg freq, harm=4, amp=0.1, out=0;
	var sig, env;
	sig = {SinOsc.ar(freq * Rand(-0.2, 0.2).midiratio)}!2;
	sig = Splay.ar(sig);
	sig = RLPF.ar(sig, (freq * harm).clip(20,20000), 0.5);
	env = EnvGen.ar(Env.perc(0.01, 0.8, 0.65), doneAction:2);
	sig = sig * env * amp;
	Out.ar(out, sig);
}).add;

MIDIdef.noteOn(\on_1, {
	arg val, num, chan, src;
	Synth(\sin, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 1);

MIDIdef.noteOn(\on_2, {
	arg val, num, chan, src;
	Synth(\perc, [
		\freq, num.midicps,
		\harm, val.lincurve(0,127,1,40,9),
		\amp, val.linlin(0,127,-40, -12).dbamp,
	]);
}, chan: 2);

MIDIdef.noteOff(\off_1, {
	Synth(\sin, [
		\gate, 0
	]);
}, chan: 1);

MIDIdef.noteOff(\off_2, {
	Synth(\perc, [
		\gate, 0
	]);
}, chan: 2);
)