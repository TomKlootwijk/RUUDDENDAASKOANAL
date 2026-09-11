; Tom Klootwijk Gambit 4.0 -- full_adder
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Bool)(declare-const b Bool)(declare-const c Bool)
(define-fun s () Bool (xor (xor a b) c))
(define-fun carry () Bool (or (and a b) (and (xor a b) c)))
(assert (not (= (+ (ite a 1 0) (ite b 1 0) (ite c 1 0)) (+ (ite s 1 0) (* 2 (ite carry 1 0))))))
(check-sat)
(get-proof)
