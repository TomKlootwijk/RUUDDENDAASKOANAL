; Tom Klootwijk Gambit 4.0 -- parity_three_word_homomorphism
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Bool)(declare-const b Bool)(declare-const c Bool)(declare-const d Bool)(declare-const e Bool)(declare-const f Bool)
(assert (not (= (xor (xor (xor a d) (xor b e)) (xor c f)) (xor (xor (xor a b) c) (xor (xor d e) f)))))
(check-sat)
(get-proof)
