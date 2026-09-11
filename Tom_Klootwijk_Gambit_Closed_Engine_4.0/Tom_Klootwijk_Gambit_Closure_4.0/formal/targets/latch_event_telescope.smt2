; Tom Klootwijk Gambit 4.0 -- latch_event_telescope
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Bool)(declare-const b Bool)(declare-const c Bool)(declare-const d Bool)
(assert (not (= (xor (xor (xor a b) (xor b c)) (xor c d)) (xor a d))))
(check-sat)
(get-proof)
