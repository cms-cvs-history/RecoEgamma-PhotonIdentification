import FWCore.ParameterSet.Config as cms

PhotonIDProd = cms.EDProducer("PhotonIDProducer",
    #required inputs
    #What collection of photons do I run on?
    photonProducer = cms.string('photons'),                              
    photonLabel = cms.string(''),
    #What labels do I use for my products?
    photonCutBasedIDLooseLabel = cms.string('PhotonCutBasedIDLoose'),
    photonCutBasedIDTightLabel = cms.string('PhotonCutBasedIDTight'),
    photonCutBasedIDLooseEMLabel=cms.string('PhotonCutBasedIDLooseEM'),
    #What rechit collection do I use for ECAL iso?                          
    doCutBased = cms.bool(True),
    #switches, turn on quality cuts for various quantities.
    RequireFiducial = cms.bool(False),
    DoHollowConeTrackIsolationCut = cms.bool(True),
    DoSolidConeTrackIsolationCut = cms.bool(False),
    DoHollowConeNTrkCut = cms.bool(False),
    DoSolidConeNTrkCut = cms.bool(False),
    DoHadOverEMCut = cms.bool(True),
    DoEtaWidthCut = cms.bool(True),
    DoHcalTowerIsolationCut = cms.bool(True),
    DoEcalRecHitIsolationCut = cms.bool(True),
    DoEcalIsoRelativeCut = cms.bool(True),
    DoR9Cut = cms.bool(False),                               
    #LooseEM cuts EB
    LooseEMEcalIsoRelativeCutSlopeEB = cms.double(0.004),
    LooseEMEcalIsoRelativeCutOffsetEB= cms.double(2.5),
    LooseEMHcalTowerIsoSlopeEB= cms.double(0.),
    LooseEMHcalTowerIsoOffsetEB=cms.double(3.),
    LooseEMHollowTrkSlopeEB=cms.double(0.),
    LooseEMHollowTrkOffsetEB=cms.double(999999999),
    LooseEMSolidTrkSlopeEB=cms.double(0.),
    LooseEMSolidTrkOffsetEB=cms.double(999999999),
    LooseEMSolidTrkEB=cms.double(999999999),
    LooseEMSolidNTrkEB=cms.int32(999999999),
    LooseEMHollowNTrkEB=cms.int32(999999999),
    LooseEMEtaWidthEB=cms.double(999999999),
    LooseEMHadOverEMEB=cms.double(0.15),
    LooseEMR9CutEB=cms.double(0.0),
    #LoosePhoton cuts EB                          
    LoosePhotonEcalIsoRelativeCutSlopeEB = cms.double(0.004),
    LoosePhotonEcalIsoRelativeCutOffsetEB= cms.double(2.5),
    LoosePhotonHcalTowerIsoSlopeEB= cms.double(0.),
    LoosePhotonHcalTowerIsoOffsetEB=cms.double(3.),
    LoosePhotonHollowTrkSlopeEB=cms.double(0.),
    LoosePhotonHollowTrkOffsetEB=cms.double(9.),
    LoosePhotonSolidTrkSlopeEB=cms.double(0.),
    LoosePhotonSolidTrkOffsetEB=cms.double(999999999),
    LoosePhotonSolidTrkEB=cms.double(999999999),
    LoosePhotonSolidNTrkEB=cms.int32(999999999),
    LoosePhotonHollowNTrkEB=cms.int32(999999999),
    LoosePhotonEtaWidthEB=cms.double(999999999),
    LoosePhotonHadOverEMEB=cms.double(0.15),
    LoosePhotonR9CutEB=cms.double(0.0),
    #TightPhoton cuts EB
    TightPhotonEcalIsoRelativeCutSlopeEB = cms.double(0.004),
    TightPhotonEcalIsoRelativeCutOffsetEB= cms.double(2.5),
    TightPhotonHcalTowerIsoSlopeEB= cms.double(0.),
    TightPhotonHcalTowerIsoOffsetEB=cms.double(3.),
    TightPhotonHollowTrkSlopeEB=cms.double(0.),
    TightPhotonHollowTrkOffsetEB=cms.double(9.),
    TightPhotonSolidTrkSlopeEB=cms.double(0.),
    TightPhotonSolidTrkOffsetEB=cms.double(999999999),
    TightPhotonSolidTrkEB=cms.double(999999999),
    TightPhotonSolidNTrkEB=cms.int32(999999999),
    TightPhotonHollowNTrkEB=cms.int32(999999999),
    TightPhotonEtaWidthEB=cms.double(0.013),
    TightPhotonHadOverEMEB=cms.double(0.15),
    TightPhotonR9CutEB=cms.double(0.0),
    #LooseEM cuts EE
    LooseEMEcalIsoRelativeCutSlopeEE = cms.double(0.0021),
    LooseEMEcalIsoRelativeCutOffsetEE= cms.double(3.),
    LooseEMHcalTowerIsoSlopeEE= cms.double(0.),
    LooseEMHcalTowerIsoOffsetEE=cms.double(3.5),
    LooseEMHollowTrkSlopeEE=cms.double(0.),
    LooseEMHollowTrkOffsetEE=cms.double(999999999),
    LooseEMSolidTrkSlopeEE=cms.double(0.),
    LooseEMSolidTrkOffsetEE=cms.double(999999999),
    LooseEMSolidTrkEE=cms.double(999999999),
    LooseEMSolidNTrkEE=cms.int32(999999999),
    LooseEMHollowNTrkEE=cms.int32(999999999),
    LooseEMEtaWidthEE=cms.double(999999999),
    LooseEMHadOverEMEE=cms.double(0.15),
    LooseEMR9CutEE=cms.double(0.0),
    #LoosePhoton cuts EE                          
    LoosePhotonEcalIsoRelativeCutSlopeEE = cms.double(0.0021),
    LoosePhotonEcalIsoRelativeCutOffsetEE= cms.double(3.),
    LoosePhotonHcalTowerIsoSlopeEE= cms.double(0.),
    LoosePhotonHcalTowerIsoOffsetEE=cms.double(3.5),
    LoosePhotonHollowTrkSlopeEE=cms.double(0.),
    LoosePhotonHollowTrkOffsetEE=cms.double(9.),
    LoosePhotonSolidTrkSlopeEE=cms.double(0.),
    LoosePhotonSolidTrkOffsetEE=cms.double(999999999),
    LoosePhotonSolidTrkEE=cms.double(999999999),
    LoosePhotonSolidNTrkEE=cms.int32(999999999),
    LoosePhotonHollowNTrkEE=cms.int32(999999999),
    LoosePhotonEtaWidthEE=cms.double(999999999),
    LoosePhotonHadOverEMEE=cms.double(0.15),
    LoosePhotonR9CutEE=cms.double(0.0),
    #TightPhoton cuts EE
    TightPhotonEcalIsoRelativeCutSlopeEE = cms.double(0.0021),
    TightPhotonEcalIsoRelativeCutOffsetEE= cms.double(5.),
    TightPhotonHcalTowerIsoSlopeEE= cms.double(0.),
    TightPhotonHcalTowerIsoOffsetEE=cms.double(5.),
    TightPhotonHollowTrkSlopeEE=cms.double(0.),
    TightPhotonHollowTrkOffsetEE=cms.double(9.),
    TightPhotonSolidTrkSlopeEE=cms.double(0.),
    TightPhotonSolidTrkOffsetEE=cms.double(999999999),
    TightPhotonSolidTrkEE=cms.double(999999999),
    TightPhotonSolidNTrkEE=cms.int32(999999999),
    TightPhotonHollowNTrkEE=cms.int32(999999999),
    TightPhotonEtaWidthEE=cms.double(999999999),
    TightPhotonHadOverEMEE=cms.double(0.15),
    TightPhotonR9CutEE=cms.double(0.0)
)


